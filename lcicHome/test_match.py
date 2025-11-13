"""
Test Script for Improved Matching Algorithm
Tests with the provided example data to verify matching improvements
"""
from datetime import date
from matching_service_improved import CustomerMatchingService


def test_example_data():
    """
    Test with the provided example data - all records are the same person
    Birth date: 1984-10-13
    Name: Khanthong/Khunthong Keokinnaly
    """
    
    # Example records from user's data
    records = [
        {
            'ind_sys_id': 2413117,
            'lcic_id': '20251106-84156',
            'segment': 'A1',
            'bnk_code': '415',
            'ind_national_id': None,
            'ind_passport': None,
            'ind_familybook': '2079018',
            'ind_familybook_prov_code': '49',
            'ind_birth_date': date(1984, 10, 13),
            'ind_name': 'Khunthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິນນາລີ',
            'ind_gender': 'M',
        },
        {
            'ind_sys_id': 2537682,
            'lcic_id': '20251106-68827',
            'segment': 'A3',
            'bnk_code': '10',
            'ind_national_id': None,
            'ind_passport': None,
            'ind_familybook': 'FA22242001',
            'ind_familybook_prov_code': '49',
            'ind_birth_date': date(1984, 10, 13),
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິນນາລີ',
            'ind_gender': 'F',  # Note: Different gender!
        },
        {
            'ind_sys_id': 1790835,
            'lcic_id': '20251106-68827',
            'segment': 'A1',
            'bnk_code': '408',
            'ind_national_id': '856130119840138',
            'ind_passport': 'P1449326',
            'ind_familybook': '1803-0023958-0',
            'ind_familybook_prov_code': None,
            'ind_birth_date': date(1984, 10, 13),
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິ່ນນາລີ',  # Slight variation
            'ind_gender': 'F',
        },
        {
            'ind_sys_id': 1888635,
            'lcic_id': '20251106-68827',
            'segment': 'A1',
            'bnk_code': '08',
            'ind_national_id': '13-0025005',
            'ind_passport': None,
            'ind_familybook': '1130025005',
            'ind_familybook_prov_code': None,
            'ind_birth_date': date(1984, 10, 13),
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິນນາລີ',
            'ind_gender': 'F',
        },
        {
            'ind_sys_id': 2224364,
            'lcic_id': '20251106-68827',
            'segment': 'A1',
            'bnk_code': '08',
            'ind_national_id': None,
            'ind_passport': None,
            'ind_familybook': '0200396712',
            'ind_familybook_prov_code': '49',
            'ind_birth_date': date(1984, 10, 13),
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິນນາລີ',
            'ind_gender': 'F',
        },
        {
            'ind_sys_id': 2218932,
            'lcic_id': '20251106-68827',
            'segment': 'A1',
            'bnk_code': '08',
            'ind_national_id': '856130119840138',  # Same as record 3
            'ind_passport': 'P2536965',
            'ind_familybook': '0101153239',
            'ind_familybook_prov_code': None,
            'ind_birth_date': date(1984, 10, 13),
            'ind_name': 'Khanthong',
            'ind_surname': 'Keokinnaly',
            'ind_lao_name': 'ຂັນທອງ',
            'ind_lao_surname': 'ແກ້ວກິນນາລີ',
            'ind_gender': 'F',
        }
    ]
    
    print("=" * 80)
    print("TESTING IMPROVED MATCHING ALGORITHM")
    print("=" * 80)
    print(f"\nTesting with {len(records)} records - all should match!\n")
    
    # Test each pair
    matches_found = 0
    total_comparisons = 0
    
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            total_comparisons += 1
            rec1 = records[i]
            rec2 = records[j]
            
            score, breakdown = CustomerMatchingService.calculate_match_score(rec1, rec2)
            
            print(f"\n{'=' * 80}")
            print(f"Comparing Record {rec1['ind_sys_id']} vs {rec2['ind_sys_id']}")
            print(f"{'=' * 80}")
            
            print(f"\n📋 Record 1 (ID: {rec1['ind_sys_id']}):")
            print(f"   Name: {rec1['ind_name']} {rec1['ind_surname']}")
            print(f"   Birth: {rec1['ind_birth_date']}")
            print(f"   Gender: {rec1['ind_gender']}")
            print(f"   National ID: {rec1['ind_national_id']}")
            print(f"   Passport: {rec1['ind_passport']}")
            print(f"   Family Book: {rec1['ind_familybook']}")
            print(f"   Bank: {rec1['bnk_code']}, Segment: {rec1['segment']}")
            
            print(f"\n📋 Record 2 (ID: {rec2['ind_sys_id']}):")
            print(f"   Name: {rec2['ind_name']} {rec2['ind_surname']}")
            print(f"   Birth: {rec2['ind_birth_date']}")
            print(f"   Gender: {rec2['ind_gender']}")
            print(f"   National ID: {rec2['ind_national_id']}")
            print(f"   Passport: {rec2['ind_passport']}")
            print(f"   Family Book: {rec2['ind_familybook']}")
            print(f"   Bank: {rec2['bnk_code']}, Segment: {rec2['segment']}")
            
            print(f"\n🎯 MATCH SCORE: {score}%")
            print(f"\n📊 Breakdown:")
            for field, field_score in breakdown.items():
                if field not in ['fields_compared', 'weights_applied', 'total_weight']:
                    print(f"   {field:20s}: {field_score:5.1f}%")
            
            print(f"\n   Fields compared: {', '.join(breakdown.get('fields_compared', []))}")
            print(f"   Total weight applied: {breakdown.get('total_weight', 0)}%")
            
            # Check if it's a match
            if score >= 60:
                matches_found += 1
                confidence = "HIGH" if score >= 85 else "MEDIUM" if score >= 70 else "LOW"
                print(f"\n✅ MATCH DETECTED - {confidence} CONFIDENCE")
            else:
                print(f"\n❌ NO MATCH - Score below threshold")
    
    print(f"\n{'=' * 80}")
    print(f"SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total comparisons: {total_comparisons}")
    print(f"Matches found (≥60%): {matches_found}")
    print(f"Match rate: {matches_found / total_comparisons * 100:.1f}%")
    print(f"\nExpected: {total_comparisons} matches (100%)")
    print(f"Result: {'✅ PASS' if matches_found == total_comparisons else '⚠️  SOME RECORDS NOT MATCHED'}")


def test_weights_comparison():
    """Compare old vs new weights"""
    
    print("\n\n" + "=" * 80)
    print("WEIGHT COMPARISON: OLD vs NEW")
    print("=" * 80)
    
    old_weights = {
        'national_id': 30,
        'passport': 25,
        'family_book': 20,
        'birth_date': 15,
        'name': 5,
        'lao_name': 5,
    }
    
    new_weights = {
        'national_id': 25,
        'passport': 20,
        'family_book': 10,
        'birth_date': 20,
        'name': 10,
        'lao_name': 7,
        'gender': 5,
        'province': 3,
    }
    
    print("\n📊 OLD WEIGHTS (Total: 100%):")
    for field, weight in sorted(old_weights.items(), key=lambda x: x[1], reverse=True):
        print(f"   {field:20s}: {weight:2d}% {'█' * weight}")
    
    print("\n📊 NEW WEIGHTS (Total: 100%):")
    for field, weight in sorted(new_weights.items(), key=lambda x: x[1], reverse=True):
        print(f"   {field:20s}: {weight:2d}% {'█' * weight}")
    
    print("\n✨ KEY IMPROVEMENTS:")
    print("   1. ⬇️  Reduced ID weights (national_id, passport, family_book)")
    print("      - Less penalty when records have different ID types")
    print("      - Family book now 10% (can be shared by siblings)")
    print("   2. ⬆️  Increased birth_date weight: 15% → 20%")
    print("      - Birth date is very reliable identifier")
    print("   3. ⬆️  Doubled name weight: 5% → 10%")
    print("      - Name matching is important for finding duplicates")
    print("   4. ⬆️  Increased lao_name weight: 5% → 7%")
    print("   5. ➕ Added gender check: 5%")
    print("      - Detects data quality issues")
    print("   6. ➕ Added province check: 3%")
    print("      - Additional validation for family books")
    print("   7. 🎯 Score normalization for missing fields")
    print("      - Better handling when records have different ID types")


if __name__ == '__main__':
    test_weights_comparison()
    test_example_data()