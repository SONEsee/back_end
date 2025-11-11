from difflib import SequenceMatcher
from datetime import datetime
from django.db import transaction
from django.db.models import Q
from typing import List, Dict, Tuple
import re
import time
from collections import defaultdict  # New: For blocking

class CustomerMatchingService:
    """Service to find and score potential customer matches"""
    
    THRESHOLD_HIGH = 85
    THRESHOLD_MEDIUM = 70
    THRESHOLD_LOW = 60
    
    WEIGHTS = {
        'national_id': 30,
        'passport': 25,
        'family_book': 20,
        'birth_date': 15,
        'name': 5,
        'lao_name': 5,
    }
    
    @staticmethod
    def normalize_string(text: str) -> str:
        """Normalize string for comparison"""
        if not text:
            return ""
        text = re.sub(r'\s+', ' ', str(text).strip().lower())
        text = re.sub(r'\b(mr|mrs|ms|miss|nang|nai)\b\.?', '', text, flags=re.IGNORECASE)
        return text.strip()
    
    @staticmethod
    def string_similarity(str1: str, str2: str) -> float:
        """Calculate similarity between two strings (0-100)"""
        if not str1 or not str2:
            return 0.0
        
        str1 = CustomerMatchingService.normalize_string(str1)
        str2 = CustomerMatchingService.normalize_string(str2)
        
        if str1 == str2:
            return 100.0
        
        ratio = SequenceMatcher(None, str1, str2).ratio()
        return round(ratio * 100, 2)
    
    @staticmethod
    def date_similarity(date1, date2, tolerance_days: int = 365) -> float:
        """Calculate date similarity (0-100)"""
        if not date1 or not date2:
            return 0.0
        
        if date1 == date2:
            return 100.0
        
        diff = abs((date1 - date2).days)
        
        if diff == 0:
            return 100.0
        elif diff <= 7:
            return 90.0
        elif diff <= 30:
            return 80.0
        elif diff <= tolerance_days:
            return max(0, 100 - (diff / tolerance_days * 100))
        else:
            return 0.0
    
    @staticmethod
    def get_block_key(record: Dict) -> Tuple[int, str, str]:
        """
        Generate block key for grouping similar records.
        - Birth decade: Reduces cross-age comparisons.
        - Surname initial: Clusters by name (English/Lao).
        - Bank code: Limits to same-bank if multi-bank data.
        This creates ~50-200 buckets, slashing pairs.
        """
        birth_decade = 0
        if record.get('ind_birth_date'):
            birth_decade = record['ind_birth_date'].year // 10  # e.g., 199 -> 19
        
        surname_initial = 'Z'  # Default
        if record.get('ind_surname'):
            surname_initial = record['ind_surname'][0].upper()
        elif record.get('ind_lao_surname'):
            surname_initial = record['ind_lao_surname'][0].upper() if record['ind_lao_surname'] else 'Z'
        
        bnk_code = record.get('bnk_code', 'UNKNOWN')
        
        return (birth_decade, surname_initial, bnk_code)
    
    @staticmethod
    def calculate_match_score(record1: Dict, record2: Dict) -> Tuple[float, Dict]:
        """Calculate overall match score between two records (with early exit)"""
        breakdown = {}
        total_score = 0.0
        
        # Early exit: Quick check on high-weight fields
        early_score = 0.0
        early_weight = 0.0
        
        # National ID (30%) - Exact/fuzzy first
        nat_id1 = record1.get('ind_national_id')
        nat_id2 = record2.get('ind_national_id')
        if nat_id1 and nat_id2:
            if nat_id1 == nat_id2:
                nat_score = 100.0
            else:
                nat_score = CustomerMatchingService.string_similarity(nat_id1, nat_id2)
            breakdown['national_id'] = nat_score
            total_score += nat_score * (CustomerMatchingService.WEIGHTS['national_id'] / 100)
            early_score += nat_score * 0.30
            early_weight += 0.30
        
        # Passport (25%) - Similar
        pass1 = record1.get('ind_passport')
        pass2 = record2.get('ind_passport')
        if pass1 and pass2:
            if pass1 == pass2:
                pass_score = 100.0
            else:
                pass_score = CustomerMatchingService.string_similarity(pass1, pass2)
            breakdown['passport'] = pass_score
            total_score += pass_score * (CustomerMatchingService.WEIGHTS['passport'] / 100)
            early_score += pass_score * 0.25
            early_weight += 0.25
        
        # Early exit if core IDs are weak
        if early_weight > 0 and (early_score / early_weight) < 50:
            return round(total_score, 2), breakdown  # Bail early, low potential
        
        # Family book (20%)
        fb1 = record1.get('ind_familybook')
        fb2 = record2.get('ind_familybook')
        if fb1 and fb2:
            if fb1 == fb2:
                fb_score = 100.0
            else:
                fb_score = CustomerMatchingService.string_similarity(fb1, fb2)
            breakdown['family_book'] = fb_score
            total_score += fb_score * (CustomerMatchingService.WEIGHTS['family_book'] / 100)
        
        # Birth date (15%)
        if record1.get('ind_birth_date') and record2.get('ind_birth_date'):
            bd_score = CustomerMatchingService.date_similarity(
                record1['ind_birth_date'], record2['ind_birth_date']
            )
            breakdown['birth_date'] = bd_score
            total_score += bd_score * (CustomerMatchingService.WEIGHTS['birth_date'] / 100)
        
        # Name (5%)
        name1 = f"{record1.get('ind_name', '')} {record1.get('ind_surname', '')}".strip()
        name2 = f"{record2.get('ind_name', '')} {record2.get('ind_surname', '')}".strip()
        if name1 and name2:
            name_score = CustomerMatchingService.string_similarity(name1, name2)
            breakdown['name'] = name_score
            total_score += name_score * (CustomerMatchingService.WEIGHTS['name'] / 100)
        
        # Lao name (5%)
        lao1 = f"{record1.get('ind_lao_name', '')} {record1.get('ind_lao_surname', '')}".strip()
        lao2 = f"{record2.get('ind_lao_name', '')} {record2.get('ind_lao_surname', '')}".strip()
        if lao1 and lao2:
            lao_score = CustomerMatchingService.string_similarity(lao1, lao2)
            breakdown['lao_name'] = lao_score
            total_score += lao_score * (CustomerMatchingService.WEIGHTS['lao_name'] / 100)
        
        return round(total_score, 2), breakdown
    
    @staticmethod
    def find_matches(IndividualBankIbk, limit: int = 1000, min_score: float = 60.0) -> List[Dict]:
        """
        Optimized: Find potential matches with blocking to reduce comparisons.
        - Fetches fewer records via DB pre-filter (exact-ish on IDs).
        - Groups into blocks, compares only within.
        - Sorts candidates by score.
        """
        from itertools import combinations
        
        start_time = time.time()
        
        # Step 1: Pre-filter at DB for records with potential (faster fetch)
        # Add partial matches on high-signal fields to skip obvious non-dups
        records_qs = IndividualBankIbk.objects.filter(
            Q(ind_national_id__isnull=False) |
            Q(ind_passport__isnull=False) |
            Q(ind_familybook__isnull=False)
        ).values(
            'ind_sys_id', 'lcic_id', 'ind_national_id', 'ind_passport', 
            'ind_familybook', 'ind_birth_date', 'ind_name', 'ind_surname',
            'ind_lao_name', 'ind_lao_surname', 'bnk_code'
        )[:limit]
        
        records = list(records_qs)  # Materialize to list for blocking
        if len(records) < 2:
            return []
        
        # Step 2: Blocking - Group similar records
        blocks = defaultdict(list)
        for record in records:
            block_key = CustomerMatchingService.get_block_key(record)
            blocks[block_key].append(record)
        
        print(f"Debug: {len(blocks)} blocks created from {len(records)} records")  # Log for tuning
        
        candidates = []
        max_pairs = 2000000  # Safety cap (tune based on your server)
        pair_count = 0
        
        # Step 3: Compare only within blocks
        for block_key, block_records in blocks.items():
            if len(block_records) < 2:
                continue
            
            for record1, record2 in combinations(block_records, 2):
                if pair_count >= max_pairs:
                    print(f"Debug: Hit pair limit {max_pairs}")
                    break
                
                if record1['ind_sys_id'] == record2['ind_sys_id']:
                    continue
                if record1.get('lcic_id') and record1['lcic_id'] == record2.get('lcic_id'):
                    continue
                
                score, breakdown = CustomerMatchingService.calculate_match_score(record1, record2)
                pair_count += 1
                
                if score >= min_score:
                    candidates.append({
                        'source_ind_sys_id': record1['ind_sys_id'],
                        'target_ind_sys_id': record2['ind_sys_id'],
                        'source_lcic_id': record1.get('lcic_id'),
                        'target_lcic_id': record2.get('lcic_id'),
                        'similarity_score': score,
                        'match_details': breakdown,
                    })
            
            if pair_count >= max_pairs:
                break
        
        print(f"Debug: Processed {pair_count} pairs")  # Log for monitoring
        
        candidates.sort(key=lambda x: x['similarity_score'], reverse=True)
        return candidates

# from difflib import SequenceMatcher
# from datetime import datetime
# from django.db import transaction
# from django.db.models import Q
# from typing import List, Dict, Tuple
# import re


# class CustomerMatchingService:
#     """Service to find and score potential customer matches"""
    
#     THRESHOLD_HIGH = 85
#     THRESHOLD_MEDIUM = 70
#     THRESHOLD_LOW = 60
    
#     WEIGHTS = {
#         'national_id': 30,
#         'passport': 25,
#         'family_book': 20,
#         'birth_date': 15,
#         'name': 5,
#         'lao_name': 5,
#     }
    
#     @staticmethod
#     def normalize_string(text: str) -> str:
#         """Normalize string for comparison"""
#         if not text:
#             return ""
#         text = re.sub(r'\s+', ' ', str(text).strip().lower())
#         text = re.sub(r'\b(mr|mrs|ms|miss|nang|nai)\b\.?', '', text, flags=re.IGNORECASE)
#         return text.strip()
    
#     @staticmethod
#     def string_similarity(str1: str, str2: str) -> float:
#         """Calculate similarity between two strings (0-100)"""
#         if not str1 or not str2:
#             return 0.0
        
#         str1 = CustomerMatchingService.normalize_string(str1)
#         str2 = CustomerMatchingService.normalize_string(str2)
        
#         if str1 == str2:
#             return 100.0
        
#         ratio = SequenceMatcher(None, str1, str2).ratio()
#         return round(ratio * 100, 2)
    
#     @staticmethod
#     def date_similarity(date1, date2, tolerance_days: int = 365) -> float:
#         """Calculate date similarity (0-100)"""
#         if not date1 or not date2:
#             return 0.0
        
#         if date1 == date2:
#             return 100.0
        
#         diff = abs((date1 - date2).days)
        
#         if diff == 0:
#             return 100.0
#         elif diff <= 7:
#             return 90.0
#         elif diff <= 30:
#             return 80.0
#         elif diff <= tolerance_days:
#             return max(0, 100 - (diff / tolerance_days * 100))
#         else:
#             return 0.0
    
#     @staticmethod
#     def calculate_match_score(record1: Dict, record2: Dict) -> Tuple[float, Dict]:
#         """Calculate overall match score between two records"""
#         breakdown = {}
#         total_score = 0.0
        
#         # National ID matching
#         if record1.get('ind_national_id') and record2.get('ind_national_id'):
#             if record1['ind_national_id'] == record2['ind_national_id']:
#                 breakdown['national_id'] = 100.0
#             else:
#                 breakdown['national_id'] = CustomerMatchingService.string_similarity(
#                     record1['ind_national_id'], 
#                     record2['ind_national_id']
#                 )
#             total_score += breakdown['national_id'] * (CustomerMatchingService.WEIGHTS['national_id'] / 100)
        
#         # Passport matching
#         if record1.get('ind_passport') and record2.get('ind_passport'):
#             if record1['ind_passport'] == record2['ind_passport']:
#                 breakdown['passport'] = 100.0
#             else:
#                 breakdown['passport'] = CustomerMatchingService.string_similarity(
#                     record1['ind_passport'], 
#                     record2['ind_passport']
#                 )
#             total_score += breakdown['passport'] * (CustomerMatchingService.WEIGHTS['passport'] / 100)
        
#         # Family book matching
#         if record1.get('ind_familybook') and record2.get('ind_familybook'):
#             if record1['ind_familybook'] == record2['ind_familybook']:
#                 breakdown['family_book'] = 100.0
#             else:
#                 breakdown['family_book'] = CustomerMatchingService.string_similarity(
#                     record1['ind_familybook'], 
#                     record2['ind_familybook']
#                 )
#             total_score += breakdown['family_book'] * (CustomerMatchingService.WEIGHTS['family_book'] / 100)
        
#         # Birth date matching
#         if record1.get('ind_birth_date') and record2.get('ind_birth_date'):
#             breakdown['birth_date'] = CustomerMatchingService.date_similarity(
#                 record1['ind_birth_date'], 
#                 record2['ind_birth_date']
#             )
#             total_score += breakdown['birth_date'] * (CustomerMatchingService.WEIGHTS['birth_date'] / 100)
        
#         # Name matching
#         name1 = f"{record1.get('ind_name', '')} {record1.get('ind_surname', '')}".strip()
#         name2 = f"{record2.get('ind_name', '')} {record2.get('ind_surname', '')}".strip()
#         if name1 and name2:
#             breakdown['name'] = CustomerMatchingService.string_similarity(name1, name2)
#             total_score += breakdown['name'] * (CustomerMatchingService.WEIGHTS['name'] / 100)
        
#         # Lao name matching
#         lao_name1 = f"{record1.get('ind_lao_name', '')} {record1.get('ind_lao_surname', '')}".strip()
#         lao_name2 = f"{record2.get('ind_lao_name', '')} {record2.get('ind_lao_surname', '')}".strip()
#         if lao_name1 and lao_name2:
#             breakdown['lao_name'] = CustomerMatchingService.string_similarity(lao_name1, lao_name2)
#             total_score += breakdown['lao_name'] * (CustomerMatchingService.WEIGHTS['lao_name'] / 100)
        
#         return round(total_score, 2), breakdown
    
#     @staticmethod
#     def find_matches(IndividualBankIbk, limit: int = 1000, min_score: float = 60.0) -> List[Dict]:
#         """Find potential matches in IndividualBankIbk table"""
#         from itertools import combinations
#         from django.db.models import Q
        
#         records = IndividualBankIbk.objects.filter(
#             Q(ind_national_id__isnull=False) |
#             Q(ind_passport__isnull=False) |
#             Q(ind_familybook__isnull=False)
#         ).values(
#             'ind_sys_id', 'lcic_id', 'ind_national_id', 'ind_passport', 
#             'ind_familybook', 'ind_birth_date', 'ind_name', 'ind_surname',
#             'ind_lao_name', 'ind_lao_surname', 'bnk_code'
#         )[:limit]
        
#         candidates = []
        
#         for record1, record2 in combinations(records, 2):
#             if record1['ind_sys_id'] == record2['ind_sys_id']:
#                 continue
#             if record1.get('lcic_id') and record1['lcic_id'] == record2.get('lcic_id'):
#                 continue
            
#             score, breakdown = CustomerMatchingService.calculate_match_score(record1, record2)
            
#             if score >= min_score:
#                 candidates.append({
#                     'source_ind_sys_id': record1['ind_sys_id'],
#                     'target_ind_sys_id': record2['ind_sys_id'],
#                     'source_lcic_id': record1.get('lcic_id'),
#                     'target_lcic_id': record2.get('lcic_id'),
#                     'similarity_score': score,
#                     'match_details': breakdown,
#                 })
        
#         candidates.sort(key=lambda x: x['similarity_score'], reverse=True)
#         return candidates
    
    @staticmethod
    def calculate_similarity(str1: str, str2: str) -> float:
        """Calculate similarity between two strings (0-100)"""
        if not str1 or not str2:
            return 0.0
        
        str1 = CustomerMatchingService.normalize_string(str1)
        str2 = CustomerMatchingService.normalize_string(str2)
        
        if str1 == str2:
            return 100.0
        
        # Use SequenceMatcher for fuzzy matching
        similarity = SequenceMatcher(None, str1, str2).ratio()
        return round(similarity * 100, 2)
    
    @staticmethod
    def calculate_name_similarity(rec1, rec2) -> float:
        """Calculate overall name similarity"""
        scores = []
        
        # English names
        if rec1.ind_name and rec2.ind_name:
            scores.append(CustomerMatchingService.calculate_similarity(
                rec1.ind_name, rec2.ind_name
            ))
        
        if rec1.ind_surname and rec2.ind_surname:
            scores.append(CustomerMatchingService.calculate_similarity(
                rec1.ind_surname, rec2.ind_surname
            ))
        
        # Lao names
        if rec1.ind_lao_name and rec2.ind_lao_name:
            scores.append(CustomerMatchingService.calculate_similarity(
                rec1.ind_lao_name, rec2.ind_lao_name
            ))
        
        if rec1.ind_lao_surname and rec2.ind_lao_surname:
            scores.append(CustomerMatchingService.calculate_similarity(
                rec1.ind_lao_surname, rec2.ind_lao_surname
            ))
        
        return round(sum(scores) / len(scores), 2) if scores else 0.0
    
    @staticmethod
    def check_birthdate_match(rec1, rec2) -> bool:
        """Check if birthdates match"""
        if not rec1.ind_birth_date or not rec2.ind_birth_date:
            return False
        return rec1.ind_birth_date == rec2.ind_birth_date
    
    @staticmethod
    def calculate_document_similarity(rec1, rec2) -> Tuple[float, Dict]:
        """Calculate document similarity and return matching details"""
        matches = []
        match_details = {}
        
        # National ID
        if rec1.ind_national_id and rec2.ind_national_id:
            if rec1.ind_national_id == rec2.ind_national_id:
                matches.append(100.0)
                match_details['national_id'] = 'exact_match'
            else:
                sim = CustomerMatchingService.calculate_similarity(
                    rec1.ind_national_id, rec2.ind_national_id
                )
                if sim > 80:
                    matches.append(sim)
                    match_details['national_id'] = f'partial_match_{sim}'
        
        # Passport
        if rec1.ind_passport and rec2.ind_passport:
            if rec1.ind_passport == rec2.ind_passport:
                matches.append(100.0)
                match_details['passport'] = 'exact_match'
            else:
                sim = CustomerMatchingService.calculate_similarity(
                    rec1.ind_passport, rec2.ind_passport
                )
                if sim > 80:
                    matches.append(sim)
                    match_details['passport'] = f'partial_match_{sim}'
        
        # Family Book
        if rec1.ind_familybook and rec2.ind_familybook:
            if rec1.ind_familybook == rec2.ind_familybook:
                matches.append(100.0)
                match_details['familybook'] = 'exact_match'
            else:
                sim = CustomerMatchingService.calculate_similarity(
                    rec1.ind_familybook, rec2.ind_familybook
                )
                if sim > 80:
                    matches.append(sim)
                    match_details['familybook'] = f'partial_match_{sim}'
        
        score = round(sum(matches) / len(matches), 2) if matches else 0.0
        return score, match_details
    
    @staticmethod
    def calculate_overall_score(name_sim: float, birthdate_match: bool, 
                               doc_sim: float) -> float:
        """Calculate weighted overall similarity score"""
        # Weights: Name 40%, Birthdate 30%, Documents 30%
        score = (
            name_sim * 0.4 +
            (100.0 if birthdate_match else 0.0) * 0.3 +
            doc_sim * 0.3
        )
        return round(score, 2)
    
    @staticmethod
    def find_matching_candidates(limit: int = 1000):
        """Find potential matching candidates from individual_bank_ibk"""
        from .models import IndividualBankIbk, MatchingCandidate
        
        # Get records that haven't been matched yet
        unmatched = IndividualBankIbk.objects.filter(
            Q(lcic_id__isnull=True) | Q(lcic_id='')
        )[:limit]
        
        candidates_created = 0
        
        for i, record1 in enumerate(unmatched):
            # Compare with records after this one to avoid duplicates
            for record2 in unmatched[i+1:]:
                # Skip if same record
                if record1.ind_sys_id == record2.ind_sys_id:
                    continue
                
                # Calculate similarities
                name_sim = CustomerMatchingService.calculate_name_similarity(
                    record1, record2
                )
                birthdate_match = CustomerMatchingService.check_birthdate_match(
                    record1, record2
                )
                doc_sim, doc_details = CustomerMatchingService.calculate_document_similarity(
                    record1, record2
                )
                overall = CustomerMatchingService.calculate_overall_score(
                    name_sim, birthdate_match, doc_sim
                )
                
                # Only create candidate if score meets threshold
                if overall >= CustomerMatchingService.REVIEW_THRESHOLD:
                    match_reasons = {
                        'name_details': {
                            'record1': {
                                'name': record1.ind_name,
                                'surname': record1.ind_surname,
                                'lao_name': record1.ind_lao_name,
                            },
                            'record2': {
                                'name': record2.ind_name,
                                'surname': record2.ind_surname,
                                'lao_name': record2.ind_lao_name,
                            }
                        },
                        'document_details': doc_details,
                        'birthdate': {
                            'record1': str(record1.ind_birth_date) if record1.ind_birth_date else None,
                            'record2': str(record2.ind_birth_date) if record2.ind_birth_date else None,
                        }
                    }
                    
                    status = 'AUTO_MATCHED' if overall >= CustomerMatchingService.AUTO_MATCH_THRESHOLD else 'PENDING'
                    
                    MatchingCandidate.objects.get_or_create(
                        source_ind_sys_id=record1.ind_sys_id,
                        target_ind_sys_id=record2.ind_sys_id,
                        defaults={
                            'name_similarity': name_sim,
                            'birthdate_match': birthdate_match,
                            'document_similarity': doc_sim,
                            'overall_score': overall,
                            'match_reasons': match_reasons,
                            'status': status,
                        }
                    )
                    candidates_created += 1
        
        return candidates_created
    
    @staticmethod
    @transaction.atomic
    def merge_customers(ind_sys_ids: List[int], performed_by: str, 
                       merge_reason: str = None) -> str:
        """
        Merge multiple customers into one normalized record
        Returns the master lcic_id
        """
        from .models import (IndividualBankIbk, IndividualBankIbkInfo, 
                           IndividualDocumentHistory, MergeHistory)
        
        # Get all records to merge
        records = IndividualBankIbk.objects.filter(
            ind_sys_id__in=ind_sys_ids
        ).order_by('ind_insert_date')
        
        if not records.exists():
            raise ValueError("No records found to merge")
        
        # Use the oldest record as master
        master = records.first()
        
        # Generate new lcic_id if not exists
        if not master.lcic_id or master.lcic_id == '':
            master.lcic_id = f"20251110-{master.ind_sys_id}"
        
        lcic_id = master.lcic_id
        
        # Create or update master record in info table
        info, created = IndividualBankIbkInfo.objects.update_or_create(
            lcic_id=lcic_id,
            defaults={
                'mm_ind_sys_id': master.mm_ind_sys_id,
                'ind_national_id': master.ind_national_id,
                'ind_national_id_date': master.ind_national_id_date,
                'ind_passport': master.ind_passport,
                'ind_passport_date': master.ind_passport_date,
                'ind_familybook': master.ind_familybook,
                'ind_familybook_prov_code': master.ind_familybook_prov_code,
                'ind_familybook_date': master.ind_familybook_date,
                'ind_birth_date': master.ind_birth_date,
                'ind_name': master.ind_name,
                'ind_surname': master.ind_surname,
                'ind_lao_name': master.ind_lao_name,
                'ind_lao_surname': master.ind_lao_surname,
            }
        )
        
        # Collect all unique documents
        documents_merged = {
            'national_ids': set(),
            'passports': set(),
            'familybooks': set(),
        }
        
        # Update all records with same lcic_id and store document history
        for record in records:
            # Update main record
            record.lcic_id = lcic_id
            record.mm_status = 'MERGED'
            record.mm_by = performed_by
            record.mm_action_date = datetime.now()
            record.save()
            
            # Store document history
            if record.ind_national_id:
                documents_merged['national_ids'].add(record.ind_national_id)
                IndividualDocumentHistory.objects.create(
                    lcic_id=lcic_id,
                    ind_national_id=record.ind_national_id,
                    ind_national_id_date=record.ind_national_id_date,
                    created_by=performed_by,
                    notes=f"Merged from ind_sys_id: {record.ind_sys_id}"
                )
            
            if record.ind_passport:
                documents_merged['passports'].add(record.ind_passport)
                IndividualDocumentHistory.objects.create(
                    lcic_id=lcic_id,
                    ind_passport=record.ind_passport,
                    ind_passport_date=record.ind_passport_date,
                    created_by=performed_by,
                    notes=f"Merged from ind_sys_id: {record.ind_sys_id}"
                )
            
            if record.ind_familybook:
                documents_merged['familybooks'].add(record.ind_familybook)
                IndividualDocumentHistory.objects.create(
                    lcic_id=lcic_id,
                    ind_familybook=record.ind_familybook,
                    ind_familybook_prov_code=record.ind_familybook_prov_code,
                    ind_familybook_date=record.ind_familybook_date,
                    created_by=performed_by,
                    notes=f"Merged from ind_sys_id: {record.ind_sys_id}"
                )
        
        # Convert sets to lists for JSON storage
        documents_merged = {
            k: list(v) for k, v in documents_merged.items()
        }
        
        # Create merge history
        MergeHistory.objects.create(
            operation='MERGE',
            master_lcic_id=lcic_id,
            merged_ind_sys_ids=ind_sys_ids,
            merge_reason=merge_reason,
            documents_merged=documents_merged,
            performed_by=performed_by
        )
        
        return lcic_id
    
    @staticmethod
    @transaction.atomic
    def unmerge_customers(ind_sys_ids: List[int], performed_by: str, 
                         reason: str = None):
        """Unmerge previously merged customers"""
        from .models import (IndividualBankIbk, MergeHistory, 
                           IndividualDocumentHistory)
        
        records = IndividualBankIbk.objects.filter(ind_sys_id__in=ind_sys_ids)
        
        if not records.exists():
            raise ValueError("No records found to unmerge")
        
        old_lcic_id = records.first().lcic_id
        
        # Reset each record
        for record in records:
            record.lcic_id = None
            record.mm_status = 'UNMERGED'
            record.mm_by = performed_by
            record.mm_action_date = datetime.now()
            record.save()
        
        # Mark document history as invalid
        IndividualDocumentHistory.objects.filter(
            lcic_id=old_lcic_id
        ).update(is_current=False, valid_to=datetime.now())
        
        # Create unmerge history
        MergeHistory.objects.create(
            operation='UNMERGE',
            master_lcic_id=old_lcic_id,
            merged_ind_sys_ids=ind_sys_ids,
            merge_reason=reason,
            performed_by=performed_by
        )