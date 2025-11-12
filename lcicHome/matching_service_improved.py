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
    Corrected matching logic:
    - Unique IDs (national_id, passport) are STRONG indicators
    - Exact ID match = Very high confidence
    - Different IDs = Strong negative (probably different people)
    - Missing IDs = Use other fields
    - Name variations are expected
    """
    
    # Confidence thresholds
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
        
        # Use sequence matcher
        ratio = SequenceMatcher(None, str1, str2).ratio()
        return round(ratio * 100, 2)
    
    @staticmethod
    def date_similarity(date1, date2) -> float:
        """Calculate date similarity - EXACT or close matches only"""
        if not date1 or not date2:
            return 0.0
        
        if date1 == date2:
            return 100.0  # EXACT match
        
        diff = abs((date1 - date2).days)
        
        # Only give credit for very close dates (likely data entry errors)
        if diff == 1:
            return 95.0
        elif diff <= 3:
            return 85.0
        elif diff <= 7:
            return 70.0
        elif diff <= 30:
            return 50.0
        else:
            return 0.0  # Different dates
    
    @staticmethod
    def calculate_match_score(record1: Dict, record2: Dict) -> Tuple[float, Dict]:
        """
        CORRECTED matching logic:
        
        1. EXACT ID matches → Very high confidence (90%+)
        2. Different IDs → Strong negative signal
        3. Missing IDs → Rely on birth date + name
        4. Names can vary but need good similarity
        """
        breakdown = {}
        score_components = []
        
        # ================================================================
        # PHASE 1: Check Unique Identifiers (National ID & Passport)
        # ================================================================
        
        nat_id1 = record1.get('ind_national_id')
        nat_id2 = record2.get('ind_national_id')
        pass1 = record1.get('ind_passport')
        pass2 = record2.get('ind_passport')
        
        has_national_id = bool(nat_id1 and nat_id2)
        has_passport = bool(pass1 and pass2)
        
        # National ID check
        if has_national_id:
            if CustomerMatchingService.exact_match(nat_id1, nat_id2):
                # EXACT match on National ID = 95% confidence (almost certainly same person)
                breakdown['national_id'] = 100.0
                breakdown['national_id_exact'] = True
                score_components.append(('national_id', 95.0))
            else:
                # Different National IDs = Different people (strong negative)
                breakdown['national_id'] = 0.0
                breakdown['national_id_exact'] = False
                # Check if they're similar (might be typo)
                similarity = CustomerMatchingService.string_similarity(nat_id1, nat_id2)
                if similarity > 85:  # Very similar (likely typo)
                    breakdown['national_id_similarity'] = similarity
                    score_components.append(('national_id', similarity * 0.8))  # Reduced confidence
                else:
                    # Too different - strong negative signal
                    return 0.0, {'reason': 'Different National IDs', 'nat_id1': nat_id1, 'nat_id2': nat_id2}
        
        # Passport check
        if has_passport:
            if CustomerMatchingService.exact_match(pass1, pass2):
                # EXACT match on Passport = 90% confidence
                breakdown['passport'] = 100.0
                breakdown['passport_exact'] = True
                score_components.append(('passport', 90.0))
            else:
                # Different Passports = Different people
                breakdown['passport'] = 0.0
                breakdown['passport_exact'] = False
                similarity = CustomerMatchingService.string_similarity(pass1, pass2)
                if similarity > 85:  # Very similar
                    breakdown['passport_similarity'] = similarity
                    score_components.append(('passport', similarity * 0.7))
                else:
                    # Too different
                    return 0.0, {'reason': 'Different Passports', 'pass1': pass1, 'pass2': pass2}
        
        # If we have exact match on either ID, that's very strong evidence
        if (has_national_id and breakdown.get('national_id_exact')) or \
           (has_passport and breakdown.get('passport_exact')):
            # Already have high confidence from ID match
            # Just verify other fields don't contradict
            pass
        
        # ================================================================
        # PHASE 2: Check Birth Date (Very Important)
        # ================================================================
        
        birth1 = record1.get('ind_birth_date')
        birth2 = record2.get('ind_birth_date')
        
        if birth1 and birth2:
            bd_score = CustomerMatchingService.date_similarity(birth1, birth2)
            breakdown['birth_date'] = bd_score
            
            if bd_score == 100:  # Exact match
                score_components.append(('birth_date', 20.0))
            elif bd_score >= 85:  # Very close
                score_components.append(('birth_date', 15.0))
            elif bd_score >= 70:  # Close
                score_components.append(('birth_date', 10.0))
            elif bd_score >= 50:  # Same month
                score_components.append(('birth_date', 5.0))
            else:
                # Very different birth dates
                # If we don't have ID match, this is problematic
                if not (has_national_id and breakdown.get('national_id_exact')) and \
                   not (has_passport and breakdown.get('passport_exact')):
                    return 0.0, {'reason': 'Different birth dates and no exact ID match'}
        
        # ================================================================
        # PHASE 3: Check Names (Expected to vary)
        # ================================================================
        
        name1 = f"{record1.get('ind_name', '')} {record1.get('ind_surname', '')}".strip()
        name2 = f"{record2.get('ind_name', '')} {record2.get('ind_surname', '')}".strip()
        
        if name1 and name2:
            name_score = CustomerMatchingService.string_similarity(name1, name2)
            breakdown['name'] = name_score
            
            # Name similarity requirements depend on whether we have ID match
            if (has_national_id and breakdown.get('national_id_exact')) or \
               (has_passport and breakdown.get('passport_exact')):
                # Have exact ID match, names just need to be reasonable
                if name_score >= 60:  # Reasonable similarity
                    score_components.append(('name', 5.0))
                elif name_score >= 40:  # Some similarity
                    score_components.append(('name', 2.0))
                else:
                    # Very different names even with ID match - suspicious
                    score_components.append(('name', -5.0))  # Penalty
            else:
                # No exact ID match, names need to be very similar
                if name_score >= 85:  # Very similar
                    score_components.append(('name', 15.0))
                elif name_score >= 70:  # Similar
                    score_components.append(('name', 10.0))
                elif name_score >= 50:  # Somewhat similar
                    score_components.append(('name', 5.0))
                else:
                    # Too different
                    return 0.0, {'reason': 'Names too different and no exact ID match'}
        
        # Lao name
        lao1 = f"{record1.get('ind_lao_name', '')} {record1.get('ind_lao_surname', '')}".strip()
        lao2 = f"{record2.get('ind_lao_name', '')} {record2.get('ind_lao_surname', '')}".strip()
        
        if lao1 and lao2:
            lao_score = CustomerMatchingService.string_similarity(lao1, lao2)
            breakdown['lao_name'] = lao_score
            
            if (has_national_id and breakdown.get('national_id_exact')) or \
               (has_passport and breakdown.get('passport_exact')):
                # Have exact ID, lao name just confirmation
                if lao_score >= 60:
                    score_components.append(('lao_name', 3.0))
            else:
                # No exact ID, lao name matters more
                if lao_score >= 85:
                    score_components.append(('lao_name', 10.0))
                elif lao_score >= 70:
                    score_components.append(('lao_name', 7.0))
                elif lao_score >= 50:
                    score_components.append(('lao_name', 3.0))
        
        # ================================================================
        # PHASE 4: Check Family Book (Can be shared)
        # ================================================================
        
        fb1 = record1.get('ind_familybook')
        fb2 = record2.get('ind_familybook')
        
        if fb1 and fb2:
            if CustomerMatchingService.exact_match(fb1, fb2):
                # Same family book - good signal but not conclusive (siblings share)
                breakdown['family_book'] = 100.0
                score_components.append(('family_book', 5.0))
            else:
                # Different family books - neutral (people can have multiple)
                breakdown['family_book'] = 0.0
        
        # Province code
        prov1 = record1.get('ind_familybook_prov_code')
        prov2 = record2.get('ind_familybook_prov_code')
        
        if prov1 and prov2:
            if CustomerMatchingService.exact_match(prov1, prov2):
                breakdown['province'] = 100.0
                score_components.append(('province', 2.0))
            else:
                breakdown['province'] = 0.0
        
        # ================================================================
        # PHASE 5: Check Gender (Should match)
        # ================================================================
        
        gender1 = record1.get('ind_gender')
        gender2 = record2.get('ind_gender')
        
        if gender1 and gender2:
            g1 = str(gender1).upper().strip()
            g2 = str(gender2).upper().strip()
            
            male_values = {'M', 'MALE', 'ຊາຍ'}
            female_values = {'F', 'FEMALE', 'ຍິງ'}
            
            g1_male = g1 in male_values
            g2_male = g2 in male_values
            g1_female = g1 in female_values
            g2_female = g2 in female_values
            
            if (g1_male and g2_male) or (g1_female and g2_female):
                # Same gender - good
                breakdown['gender'] = 100.0
                score_components.append(('gender', 2.0))
            elif (g1_male and g2_female) or (g1_female and g2_male):
                # Different gender - bad sign
                breakdown['gender'] = 0.0
                # If no exact ID match, different gender is strong negative
                if not (has_national_id and breakdown.get('national_id_exact')) and \
                   not (has_passport and breakdown.get('passport_exact')):
                    score_components.append(('gender', -10.0))  # Penalty
        
        # ================================================================
        # CALCULATE FINAL SCORE
        # ================================================================
        
        total_score = sum(score for _, score in score_components)
        
        # Ensure score is between 0-100
        total_score = max(0.0, min(100.0, total_score))
        
        breakdown['score_components'] = [
            {'field': field, 'contribution': score} 
            for field, score in score_components
        ]
        
        return round(total_score, 2), breakdown
    
    @staticmethod
    def get_block_key(record: Dict) -> Tuple:
        """
        Simplified blocking - only birth decade and surname
        """
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
        """
        Find potential matches with corrected logic
        """
        from itertools import combinations
        
        start_time = time.time()
        
        # Fetch records
        records_qs = IndividualBankIbk.objects.filter(
            Q(ind_national_id__isnull=False) |
            Q(ind_passport__isnull=False) |
            Q(ind_familybook__isnull=False)
        ).values(
            'ind_sys_id', 'lcic_id', 'segment', 'bnk_code',
            'ind_national_id', 'ind_passport', 'ind_familybook',
            'ind_familybook_prov_code', 'ind_birth_date',
            'ind_name', 'ind_surname', 'ind_lao_name', 'ind_lao_surname',
            'ind_gender', 'ind_civil_status'
        )[:limit]
        
        records = list(records_qs)
        
        if len(records) < 2:
            return []
        
        print(f"📊 Processing {len(records)} records...")
        
        # Group into blocks
        blocks = defaultdict(list)
        for record in records:
            block_key = CustomerMatchingService.get_block_key(record)
            blocks[block_key].append(record)
        
        print(f"🔍 Created {len(blocks)} blocks")
        
        # Find matches
        candidates = []
        total_comparisons = 0
        skipped_different_ids = 0
        
        for block_key, block_records in blocks.items():
            if len(block_records) < 2:
                continue
            
            for record1, record2 in combinations(block_records, 2):
                total_comparisons += 1
                
                # Skip if already merged
                if (record1.get('lcic_id') and record2.get('lcic_id') and
                    record1['lcic_id'] == record2['lcic_id']):
                    continue
                
                # Calculate score
                score, breakdown = CustomerMatchingService.calculate_match_score(
                    record1, record2
                )
                
                # Track rejections
                if score == 0 and 'reason' in breakdown:
                    skipped_different_ids += 1
                    continue
                
                # Only keep above threshold
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
                        }
                    })
        
        # Sort by score
        candidates.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        elapsed = time.time() - start_time
        
        print(f"✅ Found {len(candidates)} candidates in {elapsed:.2f}s")
        print(f"📈 Comparisons: {total_comparisons:,}")
        print(f"🚫 Skipped (different IDs): {skipped_different_ids:,}")
        
        return candidates
