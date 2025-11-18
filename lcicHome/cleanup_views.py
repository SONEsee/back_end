"""
Optimized Views for Individual Bank IBK Info Cleanup - FIXED VERSION
Handles large datasets (1M+ records) with pagination and batching
Fixed: Cache invalidation after merge operations
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q, Count, F
from django.db import transaction, connection
from django.utils import timezone
from django.core.cache import cache
from difflib import SequenceMatcher
from collections import defaultdict
import logging
import time

from .models import (
    IndividualBankIbkInfo, IndividualIdentifier, MergeHistory
)

logger = logging.getLogger(__name__)


class CleanupPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


def get_cache_version():
    """Get or create a cache version for invalidation"""
    version = cache.get('cleanup_cache_version')
    if version is None:
        version = int(time.time())
        cache.set('cleanup_cache_version', version, timeout=None)
    return version


def invalidate_cache():
    """Invalidate all cleanup caches by bumping version"""
    new_version = int(time.time())
    cache.set('cleanup_cache_version', new_version, timeout=None)
    
    # Also try to delete patterns (fallback for non-Redis)
    try:
        # Try delete_pattern if available (Redis)
        if hasattr(cache, 'delete_pattern'):
            cache.delete_pattern('cleanup_duplicates_*')
            cache.delete_pattern('name_sim_*')
        else:
            # Fallback: delete known keys
            cache.delete('cleanup_statistics')
    except Exception as e:
        logger.warning(f"Cache pattern deletion failed: {e}")
    
    logger.info(f"Cache invalidated with version: {new_version}")


def calculate_name_similarity(name1: str, name2: str) -> float:
    """Calculate similarity between two names (cached with version)"""
    if not name1 or not name2:
        return 0.0
    
    version = get_cache_version()
    cache_key = f"name_sim_v{version}_{hash(name1)}_{hash(name2)}"
    cached_result = cache.get(cache_key)
    if cached_result is not None:
        return cached_result
    
    result = SequenceMatcher(None, name1.lower(), name2.lower()).ratio() * 100
    cache.set(cache_key, result, timeout=3600)
    return result


def find_duplicates_batch(batch_size=1000, min_similarity=70.0):
    """
    Find duplicates in batches to handle large datasets
    Uses database-level optimizations and batching
    """
    total_records = IndividualBankIbkInfo.objects.count()
    
    duplicate_groups = []
    processed_ids = set()
    
    for offset in range(0, total_records, batch_size):
        batch = IndividualBankIbkInfo.objects.values(
            'ind_sys_id', 'lcic_id', 'ind_name', 'ind_surname',
            'ind_lao_name', 'ind_lao_surname', 'ind_birth_date',
            'ind_national_id', 'ind_passport', 'ind_familybook'
        ).order_by('ind_name', 'ind_surname')[offset:offset + batch_size]
        
        batch_list = list(batch)
        
        for i, record1 in enumerate(batch_list):
            if record1['ind_sys_id'] in processed_ids:
                continue
            
            group = {
                'master': record1,
                'duplicates': [],
                'similarity_scores': []
            }
            
            name1 = f"{record1['ind_name'] or ''} {record1['ind_surname'] or ''}".strip()
            lao_name1 = f"{record1['ind_lao_name'] or ''} {record1['ind_lao_surname'] or ''}".strip()
            
            for j in range(i + 1, min(i + 100, len(batch_list))):
                record2 = batch_list[j]
                
                if record2['ind_sys_id'] in processed_ids:
                    continue
                
                if record1['ind_birth_date'] != record2['ind_birth_date']:
                    continue
                
                if record1['ind_name'] and record2['ind_name']:
                    if record1['ind_name'][0].lower() != record2['ind_name'][0].lower():
                        continue
                
                name2 = f"{record2['ind_name'] or ''} {record2['ind_surname'] or ''}".strip()
                lao_name2 = f"{record2['ind_lao_name'] or ''} {record2['ind_lao_surname'] or ''}".strip()
                
                name_sim = calculate_name_similarity(name1, name2)
                lao_sim = calculate_name_similarity(lao_name1, lao_name2)
                avg_sim = (name_sim + lao_sim) / 2
                
                if avg_sim >= min_similarity:
                    group['duplicates'].append(record2)
                    group['similarity_scores'].append(avg_sim)
                    processed_ids.add(record2['ind_sys_id'])
            
            if group['duplicates']:
                processed_ids.add(record1['ind_sys_id'])
                duplicate_groups.append(group)
    
    return duplicate_groups


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_duplicate_info_records(request):
    """
    List potential duplicate records from individual_bank_ibk_info
    Optimized for large datasets with pagination
    
    Query params:
    - search: search by name, lcic_id, national_id
    - min_similarity: minimum name similarity (default 70)
    - birth_date: filter by birth date
    - name_starts_with: filter by first letter of name
    - page: page number
    - page_size: items per page (max 50)
    - use_cache: use cached results (default true)
    - force_refresh: bypass cache (default false)
    """
    try:
        search_term = request.query_params.get('search', '').strip()
        min_similarity = float(request.query_params.get('min_similarity', 70.0))
        birth_date = request.query_params.get('birth_date')
        name_starts_with = request.query_params.get('name_starts_with', '').strip().upper()
        use_cache = request.query_params.get('use_cache', 'true').lower() == 'true'
        force_refresh = request.query_params.get('force_refresh', 'false').lower() == 'true'
        
        # Generate cache key with version
        version = get_cache_version()
        cache_key = f"cleanup_duplicates_v{version}_{search_term}_{min_similarity}_{birth_date}_{name_starts_with}"
        
        # Try to get from cache (unless force_refresh)
        if use_cache and not force_refresh:
            cached_result = cache.get(cache_key)
            if cached_result:
                logger.info(f"Using cached duplicate groups (version: {version})")
                return Response(cached_result)
        
        # Build base queryset with filters
        queryset = IndividualBankIbkInfo.objects.all()
        
        if search_term:
            queryset = queryset.filter(
                Q(ind_name__icontains=search_term) |
                Q(ind_surname__icontains=search_term) |
                Q(ind_lao_name__icontains=search_term) |
                Q(ind_lao_surname__icontains=search_term) |
                Q(lcic_id__icontains=search_term) |
                Q(ind_national_id__icontains=search_term)
            )
        
        if birth_date:
            queryset = queryset.filter(ind_birth_date=birth_date)
        
        if name_starts_with:
            queryset = queryset.filter(
                Q(ind_name__istartswith=name_starts_with) |
                Q(ind_surname__istartswith=name_starts_with)
            )
        
        total_count = queryset.count()
        
        if total_count > 50000 and not (search_term or birth_date or name_starts_with):
            return Response({
                'success': False,
                'error': 'Too many records. Please apply filters (search, birth_date, or name_starts_with)',
                'total_records': total_count,
                'suggestion': 'Try filtering by birth year or first letter of name'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = queryset.order_by('ind_name', 'ind_surname')
        
        logger.info(f"Finding duplicates in {total_count} records (cache version: {version})")
        
        if total_count > 5000:
            groups = []
            batch_size = 500
            processed = set()
            
            for offset in range(0, total_count, batch_size):
                batch = list(queryset[offset:offset + batch_size])
                
                for i, record1 in enumerate(batch):
                    if record1.ind_sys_id in processed:
                        continue
                    
                    duplicates = []
                    similarity_scores = []
                    
                    name1 = f"{record1.ind_name or ''} {record1.ind_surname or ''}".strip()
                    lao_name1 = f"{record1.ind_lao_name or ''} {record1.ind_lao_surname or ''}".strip()
                    
                    for j in range(i + 1, min(i + 100, len(batch))):
                        record2 = batch[j]
                        
                        if record2.ind_sys_id in processed:
                            continue
                        
                        if record1.ind_birth_date != record2.ind_birth_date:
                            continue
                        
                        if record1.ind_name and record2.ind_name:
                            if record1.ind_name[0].lower() != record2.ind_name[0].lower():
                                continue
                        
                        name2 = f"{record2.ind_name or ''} {record2.ind_surname or ''}".strip()
                        lao_name2 = f"{record2.ind_lao_name or ''} {record2.ind_lao_surname or ''}".strip()
                        
                        name_sim = calculate_name_similarity(name1, name2)
                        lao_sim = calculate_name_similarity(lao_name1, lao_name2)
                        avg_sim = (name_sim + lao_sim) / 2
                        
                        if avg_sim >= min_similarity:
                            duplicates.append(record2)
                            similarity_scores.append(avg_sim)
                            processed.add(record2.ind_sys_id)
                    
                    if duplicates:
                        processed.add(record1.ind_sys_id)
                        
                        all_identifiers = {
                            'national_ids': set(),
                            'passports': set(),
                            'family_books': set(),
                        }
                        
                        all_records = [record1] + duplicates
                        all_ind_sys_ids = [r.ind_sys_id for r in all_records]
                        
                        for rec in all_records:
                            if rec.ind_national_id:
                                all_identifiers['national_ids'].add(rec.ind_national_id)
                            if rec.ind_passport:
                                all_identifiers['passports'].add(rec.ind_passport)
                            if rec.ind_familybook:
                                all_identifiers['family_books'].add(rec.ind_familybook)
                        
                        groups.append({
                            'group_id': f"{record1.ind_sys_id}",
                            'master_record': {
                                'ind_sys_id': record1.ind_sys_id,
                                'lcic_id': record1.lcic_id,
                                'name': f"{record1.ind_name or ''} {record1.ind_surname or ''}".strip(),
                                'lao_name': f"{record1.ind_lao_name or ''} {record1.ind_lao_surname or ''}".strip(),
                                'birth_date': record1.ind_birth_date.isoformat() if record1.ind_birth_date else None,
                                'national_id': record1.ind_national_id,
                                'passport': record1.ind_passport,
                                'family_book': record1.ind_familybook,
                            },
                            'duplicate_records': [
                                {
                                    'ind_sys_id': rec.ind_sys_id,
                                    'lcic_id': rec.lcic_id,
                                    'name': f"{rec.ind_name or ''} {rec.ind_surname or ''}".strip(),
                                    'lao_name': f"{rec.ind_lao_name or ''} {rec.ind_lao_surname or ''}".strip(),
                                    'birth_date': rec.ind_birth_date.isoformat() if rec.ind_birth_date else None,
                                    'national_id': rec.ind_national_id,
                                    'passport': rec.ind_passport,
                                    'family_book': rec.ind_familybook,
                                }
                                for rec in duplicates
                            ],
                            'duplicate_count': len(duplicates),
                            'avg_similarity': sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0,
                            'combined_identifiers': {
                                'national_ids': list(all_identifiers['national_ids']),
                                'passports': list(all_identifiers['passports']),
                                'family_books': list(all_identifiers['family_books']),
                            },
                            'all_ind_sys_ids': all_ind_sys_ids,
                        })
        else:
            groups = []
            records = list(queryset)
            processed = set()
            
            for i, record1 in enumerate(records):
                if record1.ind_sys_id in processed:
                    continue
                
                duplicates = []
                similarity_scores = []
                
                name1 = f"{record1.ind_name or ''} {record1.ind_surname or ''}".strip()
                lao_name1 = f"{record1.ind_lao_name or ''} {record1.ind_lao_surname or ''}".strip()
                
                for j in range(i + 1, len(records)):
                    record2 = records[j]
                    
                    if record2.ind_sys_id in processed:
                        continue
                    
                    if record1.ind_birth_date != record2.ind_birth_date:
                        continue
                    
                    if record1.ind_name and record2.ind_name:
                        if record1.ind_name[0].lower() != record2.ind_name[0].lower():
                            continue
                    
                    name2 = f"{record2.ind_name or ''} {record2.ind_surname or ''}".strip()
                    lao_name2 = f"{record2.ind_lao_name or ''} {record2.ind_lao_surname or ''}".strip()
                    
                    name_sim = calculate_name_similarity(name1, name2)
                    lao_sim = calculate_name_similarity(lao_name1, lao_name2)
                    avg_sim = (name_sim + lao_sim) / 2
                    
                    if avg_sim >= min_similarity:
                        duplicates.append(record2)
                        similarity_scores.append(avg_sim)
                        processed.add(record2.ind_sys_id)
                
                if duplicates:
                    processed.add(record1.ind_sys_id)
                    
                    all_identifiers = {
                        'national_ids': set(),
                        'passports': set(),
                        'family_books': set(),
                    }
                    
                    all_records = [record1] + duplicates
                    all_ind_sys_ids = [r.ind_sys_id for r in all_records]
                    
                    for rec in all_records:
                        if rec.ind_national_id:
                            all_identifiers['national_ids'].add(rec.ind_national_id)
                        if rec.ind_passport:
                            all_identifiers['passports'].add(rec.ind_passport)
                        if rec.ind_familybook:
                            all_identifiers['family_books'].add(rec.ind_familybook)
                    
                    groups.append({
                        'group_id': f"{record1.ind_sys_id}",
                        'master_record': {
                            'ind_sys_id': record1.ind_sys_id,
                            'lcic_id': record1.lcic_id,
                            'name': f"{record1.ind_name or ''} {record1.ind_surname or ''}".strip(),
                            'lao_name': f"{record1.ind_lao_name or ''} {record1.ind_lao_surname or ''}".strip(),
                            'birth_date': record1.ind_birth_date.isoformat() if record1.ind_birth_date else None,
                            'national_id': record1.ind_national_id,
                            'passport': record1.ind_passport,
                            'family_book': record1.ind_familybook,
                        },
                        'duplicate_records': [
                            {
                                'ind_sys_id': rec.ind_sys_id,
                                'lcic_id': rec.lcic_id,
                                'name': f"{rec.ind_name or ''} {rec.ind_surname or ''}".strip(),
                                'lao_name': f"{rec.ind_lao_name or ''} {rec.ind_lao_surname or ''}".strip(),
                                'birth_date': rec.ind_birth_date.isoformat() if rec.ind_birth_date else None,
                                'national_id': rec.ind_national_id,
                                'passport': rec.ind_passport,
                                'family_book': rec.ind_familybook,
                            }
                            for rec in duplicates
                        ],
                        'duplicate_count': len(duplicates),
                        'avg_similarity': sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0,
                        'combined_identifiers': {
                            'national_ids': list(all_identifiers['national_ids']),
                            'passports': list(all_identifiers['passports']),
                            'family_books': list(all_identifiers['family_books']),
                        },
                        'all_ind_sys_ids': all_ind_sys_ids,
                    })
        
        # Paginate results
        page = int(request.query_params.get('page', 1))
        page_size = min(int(request.query_params.get('page_size', 10)), 50)
        
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        
        paginated_groups = groups[start_idx:end_idx]
        
        result = {
            'success': True,
            'results': paginated_groups,
            'count': len(groups),
            'page': page,
            'page_size': page_size,
            'total_pages': (len(groups) + page_size - 1) // page_size,
            'cache_version': version,
            'from_cache': False,
        }
        
        # Cache result for 30 minutes
        if use_cache:
            cache.set(cache_key, result, timeout=1800)
        
        return Response(result)
        
    except Exception as e:
        logger.error(f"Error in list_duplicate_info_records: {str(e)}", exc_info=True)
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def merge_info_records(request):
    """
    Merge multiple info records into one master record
    FIXED: Proper cache invalidation after merge
    """
    try:
        ind_sys_ids = request.data.get('ind_sys_ids', [])
        master_ind_sys_id = request.data.get('master_ind_sys_id')
        reason = request.data.get('reason', '').strip()
        
        if not ind_sys_ids or len(ind_sys_ids) < 2:
            return Response({
                'success': False,
                'error': 'At least 2 records are required for merge'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not reason:
            return Response({
                'success': False,
                'error': 'Reason is required for merge operation'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            records = IndividualBankIbkInfo.objects.filter(
                ind_sys_id__in=ind_sys_ids
            ).select_for_update()
            
            if records.count() != len(ind_sys_ids):
                return Response({
                    'success': False,
                    'error': 'Some records not found'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            records_list = list(records)
            
            if master_ind_sys_id:
                master_record = next(
                    (r for r in records_list if r.ind_sys_id == master_ind_sys_id),
                    None
                )
                if not master_record:
                    return Response({
                        'success': False,
                        'error': 'Master record not found in selected records'
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                master_record = min(records_list, key=lambda r: r.ind_sys_id)
            
            merged_data = []
            merged_lcic_ids = set()
            all_national_ids = set()
            all_passports = set()
            all_family_books = set()
            
            for record in records_list:
                merged_lcic_ids.add(record.lcic_id)
                
                if record.ind_national_id:
                    all_national_ids.add(record.ind_national_id)
                if record.ind_passport:
                    all_passports.add(record.ind_passport)
                if record.ind_familybook:
                    all_family_books.add(record.ind_familybook)
                
                merged_data.append({
                    'ind_sys_id': record.ind_sys_id,
                    'lcic_id': record.lcic_id,
                    'name': f"{record.ind_name or ''} {record.ind_surname or ''}".strip(),
                    'lao_name': f"{record.ind_lao_name or ''} {record.ind_lao_surname or ''}".strip(),
                    'birth_date': record.ind_birth_date.isoformat() if record.ind_birth_date else None,
                    'national_id': record.ind_national_id,
                    'passport': record.ind_passport,
                    'family_book': record.ind_familybook,
                })
            
            notes = f"Merged from records: {', '.join(map(str, ind_sys_ids))}. Reason: {reason}"
            
            identifiers_to_create = []
            
            for national_id in all_national_ids:
                identifiers_to_create.append(
                    IndividualIdentifier(
                        lcic_id=master_record.lcic_id,
                        identifier_type='NATIONAL_ID',
                        identifier_value=national_id,
                        is_active=True,
                        created_by=request.user.username,
                        notes=notes
                    )
                )
            
            for passport in all_passports:
                identifiers_to_create.append(
                    IndividualIdentifier(
                        lcic_id=master_record.lcic_id,
                        identifier_type='PASSPORT',
                        identifier_value=passport,
                        is_active=True,
                        created_by=request.user.username,
                        notes=notes
                    )
                )
            
            for family_book in all_family_books:
                identifiers_to_create.append(
                    IndividualIdentifier(
                        lcic_id=master_record.lcic_id,
                        identifier_type='FAMILY_BOOK',
                        identifier_value=family_book,
                        is_active=True,
                        created_by=request.user.username,
                        notes=notes
                    )
                )
            
            IndividualIdentifier.objects.bulk_create(
                identifiers_to_create,
                ignore_conflicts=True
            )
            
            duplicate_ids = [r.ind_sys_id for r in records_list if r.ind_sys_id != master_record.ind_sys_id]
            deleted_count = IndividualBankIbkInfo.objects.filter(ind_sys_id__in=duplicate_ids).delete()[0]
            
            MergeHistory.objects.create(
                action='CLEANUP_MERGE',
                master_lcic_id=master_record.lcic_id,
                merged_ind_sys_ids=ind_sys_ids,
                merged_data={
                    'merged_records': merged_data,
                    'merged_lcic_ids': list(merged_lcic_ids),
                    'combined_identifiers': {
                        'national_ids': list(all_national_ids),
                        'passports': list(all_passports),
                        'family_books': list(all_family_books),
                    }
                },
                performed_by=request.user.username,
                reason=reason,
            )
            
            # CRITICAL FIX: Invalidate all caches
            invalidate_cache()
            
            logger.info(f"Successfully merged {len(ind_sys_ids)} records into {master_record.lcic_id}")
            
            return Response({
                'success': True,
                'message': f'Successfully merged {len(ind_sys_ids)} records',
                'master_lcic_id': master_record.lcic_id,
                'master_ind_sys_id': master_record.ind_sys_id,
                'merged_count': len(ind_sys_ids),
                'deleted_count': deleted_count,
                'identifiers_created': len(identifiers_to_create),
                'combined_identifiers': {
                    'national_ids': list(all_national_ids),
                    'passports': list(all_passports),
                    'family_books': list(all_family_books),
                },
                'cache_invalidated': True,
            })
        
    except Exception as e:
        logger.error(f"Error in merge_info_records: {str(e)}", exc_info=True)
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cleanup_statistics(request):
    """
    Get statistics for cleanup operations
    Uses versioned caching for consistency
    """
    try:
        version = get_cache_version()
        cache_key = f'cleanup_statistics_v{version}'
        
        cached_stats = cache.get(cache_key)
        if cached_stats:
            return Response({
                'success': True,
                'statistics': cached_stats,
                'cached': True,
                'cache_version': version,
            })
        
        total_records = IndividualBankIbkInfo.objects.count()
        
        recent_cleanups = MergeHistory.objects.filter(
            action='CLEANUP_MERGE'
        ).count()
        
        if total_records > 100000:
            sample_size = 10000
            sample_records = IndividualBankIbkInfo.objects.order_by('?')[:sample_size]
            
            sample_duplicates = 0
            processed = set()
            
            for record in sample_records:
                if record.ind_sys_id in processed:
                    continue
                
                similar = IndividualBankIbkInfo.objects.filter(
                    ind_birth_date=record.ind_birth_date,
                    ind_name__istartswith=record.ind_name[0] if record.ind_name else ''
                ).exclude(ind_sys_id=record.ind_sys_id)[:5]
                
                if similar.exists():
                    sample_duplicates += similar.count()
                    processed.add(record.ind_sys_id)
            
            estimated_duplicates = int((sample_duplicates / sample_size) * total_records)
            estimated_groups = int(estimated_duplicates / 2)
            
            statistics = {
                'total_records': total_records,
                'duplicate_groups': estimated_groups,
                'total_duplicates': estimated_duplicates,
                'potential_savings': estimated_duplicates - estimated_groups,
                'cleanup_merges_done': recent_cleanups,
                'is_estimate': True,
                'recommendation': 'Use filters to get exact counts for specific segments'
            }
        else:
            statistics = {
                'total_records': total_records,
                'duplicate_groups': 0,
                'total_duplicates': 0,
                'potential_savings': 0,
                'cleanup_merges_done': recent_cleanups,
                'is_estimate': False,
                'recommendation': 'Use filters to find duplicate groups'
            }
        
        cache.set(cache_key, statistics, timeout=3600)
        
        return Response({
            'success': True,
            'statistics': statistics,
            'cached': False,
            'cache_version': version,
        })
        
    except Exception as e:
        logger.error(f"Error in get_cleanup_statistics: {str(e)}", exc_info=True)
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def clear_cache(request):
    """Clear all cleanup caches"""
    try:
        invalidate_cache()
        
        return Response({
            'success': True,
            'message': 'Cache cleared successfully',
            'new_version': get_cache_version(),
        })
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)