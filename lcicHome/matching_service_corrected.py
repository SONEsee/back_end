"""
FINAL HYBRID Customer Matching Service
Balances accuracy with data quality tolerance
"""
from difflib import SequenceMatcher
from datetime import datetime
from django.db import transaction
from django.db.models import Q
from typing import List, Dict, Tuple
import re
import time
from collections import defaultdict


class CustomerMatchingService:
    """
    HYBRID matching logic:
    - Exact ID match = Very high confidence (95%+)
    - Different IDs = Check if typo (>90% similar) OR use other strong signals
    - Multiple weak signals together = Good confidence
    - Lao name codes + family book + province = Strong combination
    """
    
    THRESHOLD_HIGH = 85
    THRESHOLD_MEDIUM = 70
    THRESHOLD_LOW = 60
    
    @staticmethod
    def normalize_string(text: str) -> str:
        """Normalize string for comparison"""
        if not text:
            return ""
        text = re.sub(r'\s+', ' ', str(text).strip().lower())
        text = re.sub(r'\b(mr|mrs|ms|miss|nang|nai|ນາງ|ນາຍ)\b\.?', '', text, flags=re.IGNORECASE)
        return text.strip()
    
    @staticmethod
    def exact_match(val1: str, val2: str) -> bool:
        """Check if two values are exactly the same"""
        if not val1 or not val2:
            return False
        return str(val1).strip() == str(val2).strip()
    
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
    def date_similarity(date1, date2) -> float:
        """Calculate date similarity - RELAXED for data quality issues"""
        if not date1 or not date2:
            return 0.0
        
        if date1 == date2:
            return 100.0
        
        diff = abs((date1 - date2).days)
        
        # RELAXED: Allow up to 2 years difference (data entry errors common)
        if diff == 1:
            return 95.0
        elif diff <= 3:
            return 90.0
        elif diff <= 7:
            return 85.0
        elif diff <= 30:
            return 80.0  # Same month
        elif diff <= 365:
            return 70.0  # 1 year (likely typo)
        elif diff <= 730:
            return 60.0  # 2 years (possible typo like 1984 vs 1986)
        else:
            return 0.0
    
    @staticmethod
    def calculate_match_score(record1: Dict, record2: Dict) -> Tuple[float, Dict]:
        """
        HYBRID matching: Balance between exact matching and fuzzy matching
        """
        breakdown = {}
        score = 0.0
        
        # Get all fields
        nat_id1 = record1.get('ind_national_id')
        nat_id2 = record2.get('ind_national_id')
        pass1 = record1.get('ind_passport')
        pass2 = record2.get('ind_passport')
        birth1 = record1.get('ind_birth_date')
        birth2 = record2.get('ind_birth_date')
        
        # ================================================================
        # PHASE 1: Check for EXACT ID match (highest confidence)
        # ================================================================
        
        exact_id_match = False
        
        # Exact National ID match
        if nat_id1 and nat_id2:
            if CustomerMatchingService.exact_match(nat_id1, nat_id2):
                breakdown['national_id'] = 100.0
                breakdown['national_id_exact'] = True
                score += 95.0  # Very high confidence!
                exact_id_match = True
            else:
                # Check if very similar (might be typo)
                sim = CustomerMatchingService.string_similarity(nat_id1, nat_id2)
                breakdown['national_id'] = sim
                breakdown['national_id_exact'] = False
                
                if sim >= 90:  # Very similar - probable typo
                    score += sim * 0.8  # Give some credit
                elif sim < 50:  # Very different
                    # Don't immediately reject - check other fields
                    score += 0
                else:
                    score += sim * 0.5
        
        # Exact Passport match
        if pass1 and pass2:
            if CustomerMatchingService.exact_match(pass1, pass2):
                breakdown['passport'] = 100.0
                breakdown['passport_exact'] = True
                score += 90.0
                exact_id_match = True
            else:
                sim = CustomerMatchingService.string_similarity(pass1, pass2)
                breakdown['passport'] = sim
                breakdown['passport_exact'] = False
                if sim >= 90:
                    score += sim * 0.7
        
        # ================================================================
        # PHASE 2: Birth Date (RELAXED tolerance)
        # ================================================================
        
        if birth1 and birth2:
            bd_score = CustomerMatchingService.date_similarity(birth1, birth2)
            breakdown['birth_date'] = bd_score
            
            if exact_id_match:
                # Have ID match, birth date just confirmation
                score += bd_score * 0.1  # 10 points max
            else:
                # No ID match, birth date matters more
                if bd_score >= 90:  # Very close
                    score += 20.0
                elif bd_score >= 70:  # Close (1-2 years)
                    score += 15.0
                elif bd_score >= 50:  # Same decade
                    score += 10.0
                else:
                    score += 5.0
        
        # ================================================================
        # PHASE 3: Names (IMPORTANT when no exact ID)
        # ================================================================
        
        name1 = f"{record1.get('ind_name', '')} {record1.get('ind_surname', '')}".strip()
        name2 = f"{record2.get('ind_name', '')} {record2.get('ind_surname', '')}".strip()
        
        if name1 and name2:
            name_score = CustomerMatchingService.string_similarity(name1, name2)
            breakdown['name'] = name_score
            
            if exact_id_match:
                # Have ID, names just confirmation
                score += name_score * 0.05  # 5 points max
            else:
                # No exact ID, names very important
                if name_score >= 90:
                    score += 15.0
                elif name_score >= 80:
                    score += 12.0
                elif name_score >= 70:
                    score += 8.0
                elif name_score >= 50:
                    score += 4.0
        
        # ================================================================
        # PHASE 4: Lao Names (IMPORTANT)
        # ================================================================
        
        lao1 = f"{record1.get('ind_lao_name', '')} {record1.get('ind_lao_surname', '')}".strip()
        lao2 = f"{record2.get('ind_lao_name', '')} {record2.get('ind_lao_surname', '')}".strip()
        
        if lao1 and lao2:
            lao_score = CustomerMatchingService.string_similarity(lao1, lao2)
            breakdown['lao_name'] = lao_score
            
            if exact_id_match:
                score += lao_score * 0.03  # 3 points max
            else:
                if lao_score >= 90:
                    score += 12.0
                elif lao_score >= 80:
                    score += 10.0
                elif lao_score >= 70:
                    score += 7.0
                elif lao_score >= 50:
                    score += 3.0
        
        # ================================================================
        # PHASE 5: Lao Name CODES (NEW - Very strong signal!)
        # ================================================================
        
        lao_name_code1 = record1.get('ind_lao_name_code')
        lao_name_code2 = record2.get('ind_lao_name_code')
        lao_surname_code1 = record1.get('ind_lao_surname_code')
        lao_surname_code2 = record2.get('ind_lao_surname_code')
        
        if lao_surname_code1 and lao_surname_code2:
            if CustomerMatchingService.exact_match(lao_surname_code1, lao_surname_code2):
                breakdown['lao_surname_code'] = 100.0
                score += 10.0  # Strong signal!
            else:
                breakdown['lao_surname_code'] = 0.0
        
        if lao_name_code1 and lao_name_code2:
            if CustomerMatchingService.exact_match(lao_name_code1, lao_name_code2):
                breakdown['lao_name_code'] = 100.0
                score += 8.0  # Good signal
            else:
                breakdown['lao_name_code'] = 0.0
        
        # ================================================================
        # PHASE 6: Family Book + Province (Strong combination)
        # ================================================================
        
        fb1 = record1.get('ind_familybook')
        fb2 = record2.get('ind_familybook')
        prov1 = record1.get('ind_familybook_prov_code')
        prov2 = record2.get('ind_familybook_prov_code')
        
        if fb1 and fb2 and prov1 and prov2:
            if CustomerMatchingService.exact_match(fb1, fb2):
                breakdown['family_book'] = 100.0
                score += 8.0  # Same family book
            else:
                breakdown['family_book'] = 0.0
            
            if CustomerMatchingService.exact_match(prov1, prov2):
                breakdown['province'] = 100.0
                score += 5.0  # Same province
            else:
                breakdown['province'] = 0.0
        
        # ================================================================
        # PHASE 7: mm_ind_sys_id (OLD manual mapping)
        # ================================================================
        
        mm_id1 = record1.get('mm_ind_sys_id')
        mm_id2 = record2.get('mm_ind_sys_id')
        
        if mm_id1 and mm_id2:
            if CustomerMatchingService.exact_match(mm_id1, mm_id2):
                breakdown['mm_ind_sys_id'] = 100.0
                score += 15.0  # OLD manual match - very strong signal!
            else:
                breakdown['mm_ind_sys_id'] = 0.0
        
        # ================================================================
        # PHASE 8: Gender (WARNING flag, not blocking)
        # ================================================================
        
        gender1 = record1.get('ind_gender')
        gender2 = record2.get('ind_gender')
        
        if gender1 and gender2:
            g1 = str(gender1).upper().strip()
            g2 = str(gender2).upper().strip()
            
            male = {'M', 'MALE'}
            female = {'F', 'FEMALE'}
            
            if (g1 in male and g2 in male) or (g1 in female and g2 in female):
                breakdown['gender'] = 100.0
                score += 3.0  # Bonus for matching
            else:
                breakdown['gender'] = 0.0
                # Gender mismatch is a WARNING but not blocking
                # (too many data quality issues)
                score += 0  # No penalty
        
        # ================================================================
        # FINAL SCORE
        # ================================================================
        
        breakdown['final_score'] = round(score, 2)
        
        return round(score, 2), breakdown
    
    @staticmethod
    def get_block_key(record: Dict) -> Tuple:
        """Simplified blocking"""
        birth_decade = 0
        if record.get('ind_birth_date'):
            birth_decade = record['ind_birth_date'].year // 10
        
        surname_initial = 'Z'
        if record.get('ind_surname'):
            surname_initial = record['ind_surname'][0].upper()
        elif record.get('ind_lao_surname'):
            surname_initial = record['ind_lao_surname'][0].upper() if record['ind_lao_surname'] else 'Z'
        
        return (birth_decade, surname_initial)
    
    @staticmethod
    def find_matches(IndividualBankIbk, limit: int = 1000, min_score: float = 60.0) -> List[Dict]:
        """Find matches with HYBRID approach"""
        from itertools import combinations
        
        start_time = time.time()
        
        records_qs = IndividualBankIbk.objects.filter(
            Q(ind_national_id__isnull=False) |
            Q(ind_passport__isnull=False) |
            Q(ind_familybook__isnull=False)
        ).values(
            'ind_sys_id', 'lcic_id', 'segment', 'bnk_code',
            'mm_ind_sys_id',  # NEW: Include old manual mapping
            'ind_national_id', 'ind_passport', 'ind_familybook',
            'ind_familybook_prov_code', 'ind_birth_date',
            'ind_name', 'ind_surname', 'ind_lao_name', 'ind_lao_surname',
            'ind_lao_name_code', 'ind_lao_surname_code',  # NEW: Include codes
            'ind_gender', 'ind_civil_status'
        )[:limit]
        
        records = list(records_qs)
        
        if len(records) < 2:
            return []
        
        print(f"📊 Processing {len(records)} records...")
        
        blocks = defaultdict(list)
        for record in records:
            block_key = CustomerMatchingService.get_block_key(record)
            blocks[block_key].append(record)
        
        print(f"🔍 Created {len(blocks)} blocks")
        
        candidates = []
        total_comparisons = 0
        
        for block_key, block_records in blocks.items():
            if len(block_records) < 2:
                continue
            
            for record1, record2 in combinations(block_records, 2):
                total_comparisons += 1
                
                if (record1.get('lcic_id') and record2.get('lcic_id') and
                    record1['lcic_id'] == record2['lcic_id']):
                    continue
                
                score, breakdown = CustomerMatchingService.calculate_match_score(
                    record1, record2
                )
                
                if score >= min_score:
                    candidates.append({
                        'source_ind_sys_id': record1['ind_sys_id'],
                        'target_ind_sys_id': record2['ind_sys_id'],
                        'source_lcic_id': record1.get('lcic_id'),
                        'target_lcic_id': record2.get('lcic_id'),
                        'similarity_score': score,
                        'match_details': breakdown,
                        'source_data': {
                            'name': f"{record1.get('ind_name', '')} {record1.get('ind_surname', '')}".strip(),
                            'lao_name': f"{record1.get('ind_lao_name', '')} {record1.get('ind_lao_surname', '')}".strip(),
                            'birth_date': str(record1.get('ind_birth_date')) if record1.get('ind_birth_date') else None,
                            'gender': record1.get('ind_gender'),
                            'national_id': record1.get('ind_national_id'),
                            'passport': record1.get('ind_passport'),
                            'family_book': record1.get('ind_familybook'),
                            'bank': record1.get('bnk_code'),
                            'segment': record1.get('segment'),
                            'mm_ind_sys_id': record1.get('mm_ind_sys_id'),
                        },
                        'target_data': {
                            'name': f"{record2.get('ind_name', '')} {record2.get('ind_surname', '')}".strip(),
                            'lao_name': f"{record2.get('ind_lao_name', '')} {record2.get('ind_lao_surname', '')}".strip(),
                            'birth_date': str(record2.get('ind_birth_date')) if record2.get('ind_birth_date') else None,
                            'gender': record2.get('ind_gender'),
                            'national_id': record2.get('ind_national_id'),
                            'passport': record2.get('ind_passport'),
                            'family_book': record2.get('ind_familybook'),
                            'bank': record2.get('bnk_code'),
                            'segment': record2.get('segment'),
                            'mm_ind_sys_id': record2.get('mm_ind_sys_id'),
                        }
                    })
        
        candidates.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        elapsed = time.time() - start_time
        
        print(f"✅ Found {len(candidates)} candidates in {elapsed:.2f}s")
        print(f"📈 Comparisons: {total_comparisons:,}")
        
        return candidates