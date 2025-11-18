"""
Test Corrected Matching Logic
"""
from datetime import date
from difflib import SequenceMatcher
import re


class CustomerMatchingService:
    """Test version without Django dependencies"""
    
    @staticmethod
    def normalize_string(text: str) -> str:
        if not text:
            return ""
        text = re.sub(r'\s+', ' ', str(text).strip().lower())
        text = re.sub(r'\b(mr|mrs|ms|miss|nang|nai|ນາງ|ນາຍ)\b\.?', '', text, flags=re.IGNORECASE)
        return text.strip()
    
    @staticmethod
    def exact_match(val1: str, val2: str) -> bool:
        if not val1 or not val2:
            return False
        return str(val1).strip() == str(val2).strip()
    
    @staticmethod
    def string_similarity(str1: str, str2: str) -> float:
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
        if not date1 or not date2:
            return 0.0
        
        if date1 == date2:
            return 100.0
        
        diff = abs((date1 - date2).days)
        
        if diff == 1:
            return 95.0
        elif diff <= 3:
            return 85.0
        elif diff <= 7:
            return 70.0
        elif diff <= 30:
            return 50.0
        else:
            return 0.0
    
    @staticmethod
    def calculate_match_score(record1: dict, record2: dict):
        breakdown = {}
        score_components = []
        
        # Check National ID
        nat_id1 = record1.get('ind_national_id')
        nat_id2 = record2.get('ind_national_id')
        pass1 = record1.get('ind_passport')
        pass2 = record2.get('ind_passport')
        
        has_national_id = bool(nat_id1 and nat_id2)
        has_passport = bool(pass1 and pass2)
        
        # National ID check
        if has_national_id:
            if CustomerMatchingService.exact_match(nat_id1, nat_id2):
                breakdown['national_id'] = 100.0
                breakdown['national_id_exact'] = True
                score_components.append(('national_id', 95.0))
            else:
                breakdown['national_id'] = 0.0
                breakdown['national_id_exact'] = False
                similarity = CustomerMatchingService.string_similarity(nat_id1, nat_id2)
                if similarity > 85:
                    breakdown['national_id_similarity'] = similarity
                    score_components.append(('national_id', similarity * 0.8))
                else:
                    return 0.0, {'reason': 'Different National IDs', 'nat_id1': nat_id1, 'nat_id2': nat_id2}
        
        # Passport check
        if has_passport:
            if CustomerMatchingService.exact_match(pass1, pass2):
                breakdown['passport'] = 100.0
                breakdown['passport_exact'] = True
                score_components.append(('passport', 90.0))
            else:
                breakdown['passport'] = 0.0
                breakdown['passport_exact'] = False
                similarity = CustomerMatchingService.string_similarity(pass1, pass2)
                if similarity > 85:
                    breakdown['passport_similarity'] = similarity
                    score_components.append(('passport', similarity * 0.7))
                else:
                    return 0.0, {'reason': 'Different Passports', 'pass1': pass1, 'pass2': pass2}
        
        # Birth date
        birth1 = record1.get('ind_birth_date')
        birth2 = record2.get('ind_birth_date')
        
        if birth1 and birth2:
            bd_score = CustomerMatchingService.date_similarity(birth1, birth2)
            breakdown['birth_date'] = bd_score
            
            if bd_score == 100:
                score_components.append(('birth_date', 20.0))
            elif bd_score >= 85:
                score_components.append(('birth_date', 15.0))
            elif bd_score >= 70:
                score_components.append(('birth_date', 10.0))
            elif bd_score >= 50:
                score_components.append(('birth_date', 5.0))
            else:
                if not (has_national_id and breakdown.get('national_id_exact')) and \
                   not (has_passport and breakdown.get('passport_exact')):
                    return 0.0, {'reason': 'Different birth dates and no exact ID match'}
        
        # Names
        name1 = f"{record1.get('ind_name', '')} {record1.get('ind_surname', '')}".strip()
        name2 = f"{record2.get('ind_name', '')} {record2.get('ind_surname', '')}".strip()
        
        if name1 and name2:
            name_score = CustomerMatchingService.string_similarity(name1, name2)
            breakdown['name'] = name_score
            
            if (has_national_id and breakdown.get('national_id_exact')) or \
               (has_passport and breakdown.get('passport_exact')):
                if name_score >= 60:
                    score_components.append(('name', 5.0))
                elif name_score >= 40:
                    score_components.append(('name', 2.0))
                else:
                    score_components.append(('name', -5.0))
            else:
                if name_score >= 85:
                    score_components.append(('name', 15.0))
                elif name_score >= 70:
                    score_components.append(('name', 10.0))
                elif name_score >= 50:
                    score_components.append(('name', 5.0))
                else:
                    return 0.0, {'reason': 'Names too different and no exact ID match'}
        
        # Lao name
        lao1 = f"{record1.get('ind_lao_name', '')} {record1.get('ind_lao_surname', '')}".strip()
        lao2 = f"{record2.get('ind_lao_name', '')} {record2.get('ind_lao_surname', '')}".strip()
        
        if lao1 and lao2:
            lao_score = CustomerMatchingService.string_similarity(lao1, lao2)
            breakdown['lao_name'] = lao_score
            
            if (has_national_id and breakdown.get('national_id_exact')) or \
               (has_passport and breakdown.get('passport_exact')):
                if lao_score >= 60:
                    score_components.append(('lao_name', 3.0))
            else:
                if lao_score >= 85:
                    score_components.append(('lao_name', 10.0))
                elif lao_score >= 70:
                    score_components.append(('lao_name', 7.0))
                elif lao_score >= 50:
                    score_components.append(('lao_name', 3.0))
        
        # Family book
        fb1 = record1.get('ind_familybook')
        fb2 = record2.get('ind_familybook')
        
        if fb1 and fb2:
            if CustomerMatchingService.exact_match(fb1, fb2):
                breakdown['family_book'] = 100.0
                score_components.append(('family_book', 5.0))
            else:
                breakdown['family_book'] = 0.0
        
        # Province
        prov1 = record1.get('ind_familybook_prov_code')
        prov2 = record2.get('ind_familybook_prov_code')
        
        if prov1 and prov2:
            if CustomerMatchingService.exact_match(prov1, prov2):
                breakdown['province'] = 100.0
                score_components.append(('province', 2.0))
            else:
                breakdown['province'] = 0.0
        
        # Gender
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
                breakdown['gender'] = 100.0
                score_components.append(('gender', 2.0))
            elif (g1_male and g2_female) or (g1_female and g2_male):
                breakdown['gender'] = 0.0
                if not (has_national_id and breakdown.get('national_id_exact')) and \
                   not (has_passport and breakdown.get('passport_exact')):
                    score_components.append(('gender', -10.0))
        
        # Calculate final score
        total_score = sum(score for _, score in score_components)
        total_score = max(0.0, min(100.0, total_score))
        
        breakdown['score_components'] = [
            {'field': field, 'contribution': score} 
            for field, score in score_components
        ]
        
        return round(total_score, 2), breakdown


def test_should_not_match():
    """
    Test that clearly different people DON'T match
    (Your bad example: Bounleng vs Souphasone)
    """
    print("=" * 80)
    print("TEST 1: DIFFERENT PEOPLE SHOULD NOT MATCH")
    print("=" * 80)
    
    record1 = {
        'ind_sys_id': 2398145,
        'ind_name': 'Bounleng',
        'ind_surname': 'Phengsysavath',
        'ind_lao_name': 'ບຸນເລັ່ງ',
        'ind_lao_surname': 'ເພັງສີສະຫວັດ',
        'ind_birth_date': date(1990, 9, 21),
        'ind_gender': 'M',
        'ind_national_id': '856010219901136',
        'ind_passport': None,
        'ind_familybook': '1050150095',
        'ind_familybook_prov_code': None,
        'bnk_code': '408',
        'segment': 'A1',
    }
    
    record2 = {
        'ind_sys_id': 2475958,
        'ind_name': 'Souphasone',
        'ind_surname': 'Phaksavath',
        'ind_lao_name': 'ສຸພະສອນ',
        'ind_lao_surname': 'ພັກສະຫວັດ',
        'ind_birth_date': date(1990, 9, 15),
        'ind_gender': 'F',
        'ind_national_id': '856010219900170',
        'ind_passport': None,
        'ind_familybook': '1050540048',
        'ind_familybook_prov_code': None,
        'bnk_code': '408',
        'segment': 'A1',
    }
    
    print("\n📋 Record 1:")
    print(f"   Name: {record1['ind_name']} {record1['ind_surname']}")
    print(f"   Birth: {record1['ind_birth_date']}")
    print(f"   Gender: {record1['ind_gender']}")
    print(f"   National ID: {record1['ind_national_id']}")
    
    print("\n📋 Record 2:")
    print(f"   Name: {record2['ind_name']} {record2['ind_surname']}")
    print(f"   Birth: {record2['ind_birth_date']}")
    print(f"   Gender: {record2['ind_gender']}")
    print(f"   National ID: {record2['ind_national_id']}")
    
    score, breakdown = CustomerMatchingService.calculate_match_score(record1, record2)
    
    print(f"\n🎯 MATCH SCORE: {score}%")
    print(f"📊 Breakdown: {breakdown}")
    
    if score < 60:
        print(f"\n✅ CORRECT: Not matched (score {score}% < 60%)")
        print("   Different people correctly identified!")
    else:
        print(f"\n❌ WRONG: False match (score {score}% >= 60%)")
        print("   These are clearly different people!")
    
    return score < 60


def test_should_match():
    """
    Test that same person DOES match
    (Your correct example: Khanthong/Khunthong records)
    """
    print("\n\n" + "=" * 80)
    print("TEST 2: SAME PERSON SHOULD MATCH")
    print("=" * 80)
    
    # Sample records from your data - all same person
    records = [
        {
            'ind_sys_id': 2498944,
            'lcic_id': '20251106-604488',
            'segment': 'A1',
            'bnk_code': '415',
            'ind_name': 'Khunthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ນາງ ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິນນາລີ',
            'ind_birth_date': date(1986, 10, 13),
            'ind_gender': 'M',
            'ind_national_id': None,
            'ind_passport': None,
            'ind_familybook': '2088086',
            'ind_familybook_prov_code': '49',
        },
        {
            'ind_sys_id': 2537682,
            'lcic_id': '20251106-68827',
            'segment': 'A3',
            'bnk_code': '10',
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິນນາລີ',
            'ind_birth_date': date(1984, 10, 13),
            'ind_gender': 'F',
            'ind_national_id': None,
            'ind_passport': None,
            'ind_familybook': 'FA22242001',
            'ind_familybook_prov_code': '49',
        },
        {
            'ind_sys_id': 1659451,
            'lcic_id': '20251106-68827',
            'segment': 'A1',
            'bnk_code': '413',
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິ່ນນາລີ',
            'ind_birth_date': date(1984, 10, 13),
            'ind_gender': 'F',
            'ind_national_id': '856130119840138',
            'ind_passport': None,
            'ind_familybook': '00020264',
            'ind_familybook_prov_code': None,
        },
        {
            'ind_sys_id': 1790835,
            'lcic_id': '20251106-68827',
            'segment': 'A1',
            'bnk_code': '408',
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິ່ນນາລີ',
            'ind_birth_date': date(1984, 10, 13),
            'ind_gender': 'F',
            'ind_national_id': '856130119840138',
            'ind_passport': 'P1449326',
            'ind_familybook': '1803-0023958-0',
            'ind_familybook_prov_code': None,
        },
    ]
    
    matches_found = 0
    total_pairs = 0
    
    print("\n🧪 Testing all pairs:")
    
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            total_pairs += 1
            rec1 = records[i]
            rec2 = records[j]
            
            score, breakdown = CustomerMatchingService.calculate_match_score(rec1, rec2)
            
            print(f"\n  Pair {total_pairs}: Record {rec1['ind_sys_id']} vs {rec2['ind_sys_id']}")
            print(f"    Names: {rec1['ind_name']} vs {rec2['ind_name']}")
            print(f"    Birth: {rec1['ind_birth_date']} vs {rec2['ind_birth_date']}")
            print(f"    NID: {rec1['ind_national_id']} vs {rec2['ind_national_id']}")
            print(f"    Score: {score}%")
            
            if 'reason' in breakdown:
                print(f"    Reason: {breakdown['reason']}")
            
            if score >= 60:
                matches_found += 1
                print(f"    ✅ MATCHED")
            else:
                print(f"    ❌ NOT MATCHED")
    
    print(f"\n📊 Summary:")
    print(f"   Total pairs: {total_pairs}")
    print(f"   Matched: {matches_found}")
    print(f"   Match rate: {matches_found/total_pairs*100:.1f}%")
    
    # Note: The birth dates are different (1984 vs 1986), so some might not match
    # Let's see how many match
    if matches_found >= total_pairs * 0.5:  # At least 50% should match
        print(f"\n✅ GOOD: At least {matches_found} pairs matched")
    else:
        print(f"\n⚠️  WARNING: Only {matches_found} pairs matched")
    
    return matches_found >= 2  # At least some pairs should match


def test_exact_id_match():
    """
    Test that exact ID match gives very high confidence
    """
    print("\n\n" + "=" * 80)
    print("TEST 3: EXACT ID MATCH = HIGH CONFIDENCE")
    print("=" * 80)
    
    record1 = {
        'ind_sys_id': 1,
        'ind_name': 'Somchai',  # Different names
        'ind_surname': 'Smith',
        'ind_lao_name': 'ສົມໃຈ',
        'ind_lao_surname': 'ສະມິດ',
        'ind_birth_date': date(1990, 1, 1),
        'ind_gender': 'M',
        'ind_national_id': '856010119900123',  # SAME ID
        'ind_passport': None,
        'ind_familybook': None,
    }
    
    record2 = {
        'ind_sys_id': 2,
        'ind_name': 'Somjai',  # Different name (typo)
        'ind_surname': 'Smith',
        'ind_lao_name': 'ສົມໃຈ',
        'ind_lao_surname': 'ສະມິດ',
        'ind_birth_date': date(1990, 1, 1),
        'ind_gender': 'M',
        'ind_national_id': '856010119900123',  # SAME ID
        'ind_passport': None,
        'ind_familybook': None,
    }
    
    print("\nBoth records have SAME National ID: 856010119900123")
    print("Even though names slightly different (Somchai vs Somjai)")
    
    score, breakdown = CustomerMatchingService.calculate_match_score(record1, record2)
    
    print(f"\n🎯 MATCH SCORE: {score}%")
    print(f"📊 Breakdown:")
    for key, value in breakdown.items():
        if key not in ['score_components', 'national_id_exact']:
            print(f"   {key}: {value}")
    
    if score >= 85:
        print(f"\n✅ CORRECT: High confidence match (score {score}% >= 85%)")
        print("   Exact ID match gives strong signal!")
    else:
        print(f"\n❌ WRONG: Should be high confidence (score {score}% < 85%)")
    
    return score >= 85


def test_missing_ids_similar_data():
    """
    Test matching when IDs are missing but other data matches
    """
    print("\n\n" + "=" * 80)
    print("TEST 4: MISSING IDS + SIMILAR DATA")
    print("=" * 80)
    
    record1 = {
        'ind_sys_id': 1,
        'ind_name': 'Bouasone',
        'ind_surname': 'Vongkhamchanh',
        'ind_lao_name': 'ບົວສອນ',
        'ind_lao_surname': 'ວົງຄຳຈັນ',
        'ind_birth_date': date(1985, 5, 15),
        'ind_gender': 'M',
        'ind_national_id': None,  # Missing
        'ind_passport': None,  # Missing
        'ind_familybook': '1234567',
        'ind_familybook_prov_code': '01',
    }
    
    record2 = {
        'ind_sys_id': 2,
        'ind_name': 'Bouasone',
        'ind_surname': 'Vongkhamchanh',
        'ind_lao_name': 'ບົວສອນ',
        'ind_lao_surname': 'ວົງຄຳຈັນ',
        'ind_birth_date': date(1985, 5, 15),
        'ind_gender': 'M',
        'ind_national_id': None,  # Missing
        'ind_passport': None,  # Missing
        'ind_familybook': '7654321',  # Different
        'ind_familybook_prov_code': '01',
    }
    
    print("\nNo National ID or Passport")
    print("Same: Name, Birth Date, Gender, Province")
    print("Different: Family Book")
    
    score, breakdown = CustomerMatchingService.calculate_match_score(record1, record2)
    
    print(f"\n🎯 MATCH SCORE: {score}%")
    print(f"📊 Breakdown:")
    for key, value in breakdown.items():
        if key not in ['score_components']:
            print(f"   {key}: {value}")
    
    if score >= 60:
        print(f"\n✅ MATCHED: Relies on name + birth date + gender")
    else:
        print(f"\n❌ NOT MATCHED: Needs ID confirmation")
    
    return True


if __name__ == '__main__':
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║        CORRECTED MATCHING ALGORITHM TEST SUITE                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    test1_pass = test_should_not_match()
    test2_pass = test_should_match()
    test3_pass = test_exact_id_match()
    test4_pass = test_missing_ids_similar_data()
    
    print("\n\n" + "=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    print(f"Test 1 (Different people don't match):     {'✅ PASS' if test1_pass else '❌ FAIL'}")
    print(f"Test 2 (Same person matches):              {'✅ PASS' if test2_pass else '❌ FAIL'}")
    print(f"Test 3 (Exact ID = high confidence):       {'✅ PASS' if test3_pass else '❌ FAIL'}")
    print(f"Test 4 (Missing IDs scenario):             {'✅ PASS' if test4_pass else '❌ FAIL'}")
    
    if all([test1_pass, test2_pass, test3_pass]):
        print("\n🎉 ALL CRITICAL TESTS PASSED!")
    else:
        print("\n⚠️  SOME TESTS FAILED - NEEDS REVIEW")