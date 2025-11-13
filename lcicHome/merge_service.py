"""
Customer Merge Service
Handles merging and unmerging customer records
"""
from typing import List, Dict
from django.db import transaction
from django.utils import timezone
from datetime import datetime


class CustomerMergeService:
    """
    Service to merge and unmerge customer records
    """
    
    @staticmethod
    def generate_lcic_id() -> str:
        """Generate unique LCIC ID"""
        today = datetime.now().strftime('%Y%m%d')
        from random import randint
        random_num = randint(10000, 99999)
        return f"{today}-{random_num}"
    
    @staticmethod
    @transaction.atomic
    def merge_customers(
        IndividualBankIbk,
        IndividualBankIbkInfo,
        IndividualIdentifier,
        MergeHistory,
        source_ids: List[int],
        master_record_id: int = None,
        performed_by: str = 'system',
        reason: str = None
    ) -> Dict:
        """
        Merge multiple customer records into one
        
        Args:
            source_ids: List of ind_sys_id to merge
            master_record_id: Which record to use as master (if None, use first)
            performed_by: Username performing the merge
            reason: Reason for merge
            
        Returns:
            Dict with merge results
        """
        if len(source_ids) < 2:
            raise ValueError("At least 2 records required for merge")
        
        # Get source records
        source_records = IndividualBankIbk.objects.filter(
            ind_sys_id__in=source_ids
        ).order_by('ind_sys_id')
        
        if not source_records.exists():
            raise ValueError("Source records not found")
        
        # Determine master record
        if master_record_id:
            master_record = source_records.filter(ind_sys_id=master_record_id).first()
            if not master_record:
                raise ValueError("Master record not found")
        else:
            master_record = source_records.first()
        
        # Generate or use existing LCIC ID
        lcic_id = master_record.lcic_id or CustomerMergeService.generate_lcic_id()
        
        # Collect all unique identifiers
        identifiers = []
        merged_data = []
        
        for record in source_records:
            # Store record snapshot
            merged_data.append({
                'ind_sys_id': record.ind_sys_id,
                'ind_national_id': record.ind_national_id,
                'ind_passport': record.ind_passport,
                'ind_familybook': record.ind_familybook,
                'ind_name': record.ind_name,
                'ind_surname': record.ind_surname,
                'bnk_code': record.bnk_code,
            })
            
            # Collect national ID
            if record.ind_national_id:
                identifiers.append({
                    'type': 'NATIONAL_ID',
                    'value': record.ind_national_id,
                    'date': record.ind_national_id_date,
                })
            
            # Collect passport
            if record.ind_passport:
                identifiers.append({
                    'type': 'PASSPORT',
                    'value': record.ind_passport,
                    'date': record.ind_passport_date,
                })
            
            # Collect family book
            if record.ind_familybook:
                identifiers.append({
                    'type': 'FAMILY_BOOK',
                    'value': record.ind_familybook,
                    'date': record.ind_familybook_date,
                    'province_code': record.ind_familybook_prov_code,
                })
            
            # Update source record with master LCIC ID
            record.lcic_id = lcic_id
            record.mm_ind_sys_id = str(master_record.ind_sys_id)
            record.mm_status = 'MERGED'
            record.mm_action_date = timezone.now()
            record.mm_by = performed_by
            record.save()
        
        # Remove duplicates from identifiers
        unique_identifiers = []
        seen = set()
        for ident in identifiers:
            key = f"{ident['type']}_{ident['value']}"
            if key not in seen:
                seen.add(key)
                unique_identifiers.append(ident)
        
        # Create or update in IndividualBankIbkInfo
        info_record, created = IndividualBankIbkInfo.objects.update_or_create(
            lcic_id=lcic_id,
            defaults={
                'mm_ind_sys_id': str(master_record.ind_sys_id),
                'ind_national_id': master_record.ind_national_id,
                'ind_national_id_date': master_record.ind_national_id_date,
                'ind_passport': master_record.ind_passport,
                'ind_passport_date': master_record.ind_passport_date,
                'ind_familybook': master_record.ind_familybook,
                'ind_familybook_prov_code': master_record.ind_familybook_prov_code,
                'ind_familybook_date': master_record.ind_familybook_date,
                'ind_birth_date': master_record.ind_birth_date,
                'ind_name': master_record.ind_name,
                'ind_surname': master_record.ind_surname,
                'ind_lao_name': master_record.ind_lao_name,
                'ind_lao_surname': master_record.ind_lao_surname,
            }
        )
        
        # Store all identifiers in one-to-many table
        for ident in unique_identifiers:
            IndividualIdentifier.objects.get_or_create(
                lcic_id=lcic_id,
                identifier_type=ident['type'],
                identifier_value=ident['value'],
                is_active=True,
                defaults={
                    'identifier_date': ident.get('date'),
                    'province_code': ident.get('province_code'),
                    'created_by': performed_by,
                    'notes': f"Merged from records: {', '.join(map(str, source_ids))}"
                }
            )
        
        # Log merge history
        MergeHistory.objects.create(
            action='MERGE',
            master_lcic_id=lcic_id,
            merged_ind_sys_ids=source_ids,
            merged_data=merged_data,
            performed_by=performed_by,
            reason=reason,
        )
        
        return {
            'success': True,
            'lcic_id': lcic_id,
            'master_ind_sys_id': master_record.ind_sys_id,
            'merged_count': len(source_ids),
            'identifiers_count': len(unique_identifiers),
        }
    
    @staticmethod
    @transaction.atomic
    def unmerge_customer(
        IndividualBankIbk,
        IndividualIdentifier,
        MergeHistory,
        ind_sys_id: int,
        performed_by: str = 'system',
        reason: str = None
    ) -> Dict:
        """
        Unmerge a specific customer record
        
        Args:
            ind_sys_id: The ind_sys_id to unmerge
            performed_by: Username performing the unmerge
            reason: Reason for unmerge
            
        Returns:
            Dict with unmerge results
        """
        # Get the record
        record = IndividualBankIbk.objects.filter(ind_sys_id=ind_sys_id).first()
        if not record:
            raise ValueError("Record not found")
        
        old_lcic_id = record.lcic_id
        
        # Generate new LCIC ID
        new_lcic_id = CustomerMergeService.generate_lcic_id()
        
        # Update record
        record.lcic_id = new_lcic_id
        record.mm_ind_sys_id = str(ind_sys_id)
        record.mm_status = 'UNMERGED'
        record.mm_action_date = timezone.now()
        record.mm_by = performed_by
        record.save()
        
        # Move identifiers to new LCIC ID
        old_identifiers = IndividualIdentifier.objects.filter(
            lcic_id=old_lcic_id,
            is_active=True
        )
        
        moved_identifiers = []
        for ident in old_identifiers:
            # Check if this identifier belongs to the unmerged record
            should_move = False
            if ident.identifier_type == 'NATIONAL_ID' and ident.identifier_value == record.ind_national_id:
                should_move = True
            elif ident.identifier_type == 'PASSPORT' and ident.identifier_value == record.ind_passport:
                should_move = True
            elif ident.identifier_type == 'FAMILY_BOOK' and ident.identifier_value == record.ind_familybook:
                should_move = True
            
            if should_move:
                # Deactivate old
                ident.is_active = False
                ident.deactivated_at = timezone.now()
                ident.deactivated_by = performed_by
                ident.save()
                
                # Create new
                IndividualIdentifier.objects.create(
                    lcic_id=new_lcic_id,
                    identifier_type=ident.identifier_type,
                    identifier_value=ident.identifier_value,
                    identifier_date=ident.identifier_date,
                    province_code=ident.province_code,
                    is_active=True,
                    created_by=performed_by,
                    notes=f"Unmerged from {old_lcic_id}"
                )
                moved_identifiers.append(ident.identifier_value)
        
        # Log unmerge history
        MergeHistory.objects.create(
            action='UNMERGE',
            master_lcic_id=new_lcic_id,
            merged_ind_sys_ids=[ind_sys_id],
            merged_data=[{
                'old_lcic_id': old_lcic_id,
                'new_lcic_id': new_lcic_id,
                'ind_sys_id': ind_sys_id,
            }],
            performed_by=performed_by,
            reason=reason,
        )
        
        return {
            'success': True,
            'old_lcic_id': old_lcic_id,
            'new_lcic_id': new_lcic_id,
            'ind_sys_id': ind_sys_id,
            'moved_identifiers': moved_identifiers,
        }
    
    @staticmethod
    def get_merge_candidates_summary(MatchingCandidate) -> Dict:
        """
        Get summary statistics of matching candidates
        """
        from django.db.models import Count, Avg, Max, Min
        
        stats = MatchingCandidate.objects.aggregate(
            total=Count('id'),
            pending=Count('id', filter=Q(status='PENDING')),
            approved=Count('id', filter=Q(status='APPROVED')),
            rejected=Count('id', filter=Q(status='REJECTED')),
            avg_score=Avg('similarity_score'),
            max_score=Max('similarity_score'),
            min_score=Min('similarity_score'),
        )
        
        return stats