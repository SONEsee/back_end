from django.db import transaction
from django.db.models import Q
from datetime import datetime
from .models import (
    CompanyInfoMapping,
    EnterprisCodeMaping,
    TaxNoMaping,
    NameEnterpresEnMaping,
    NameEnterpresLaMaping,
    NameLaCodeEnterpriseMaping,
    EnterpriseLookLikeMaping
)

class CompanyMappingService:
    
    # Mapping ລະຫວ່າງ code ກັບ Model
    CODE_MODEL_MAPPING = {
        'ci': EnterprisCodeMaping,
        'ct': TaxNoMaping,
        'ce': NameEnterpresEnMaping,
        'cl': NameEnterpresLaMaping,
        'clc': NameLaCodeEnterpriseMaping,
        'ctt': EnterpriseLookLikeMaping,
    }
    
    @staticmethod
    @transaction.atomic
    def merge_company_mappings_with_logging(
        mapping_pairs: list[dict],
        master_pair: dict,
        code: str,
        user: str = None
    ):
        """
        ອັບເດດ com_enterprise_code ແລະ LCIC_code ແລະບັນທຶກໄປຍັງຕາຕະລາງຕາມ code
        
        Parameters:
        -----------
        mapping_pairs: list[dict]
            ລາຍການຄູ່ທີ່ຕ້ອງການອັບເດດ
            ຕົວຢ່າງ: [
                {'com_enterprise_code': 'ENT001', 'LCIC_code': 'LCIC001'},
                {'com_enterprise_code': 'ENT002', 'LCIC_code': 'LCIC002'},
            ]
            
        master_pair: dict
            ຄູ່ທີ່ເປັນຫຼັກສຳລັບອັບເດດ
            ຕົວຢ່າງ: {'com_enterprise_code': 'ENT001', 'LCIC_code': 'LCIC001'}
            
        code: str
            ລະຫັດສຳລັບກຳນົດຕາຕະລາງທີ່ຈະບັນທຶກ
            ຕົວເລືອກ: 'ci', 'ct', 'ce', 'cl', 'clc', 'ctt'
            
        user: str
            ຜູ້ໃຊ້ທີ່ດຳເນີນການ
            
        Returns:
        --------
        dict: ສະຫຼຸບຜົນການອັບເດດ
        """
        
        # ກວດສອບ code
        if code not in CompanyMappingService.CODE_MODEL_MAPPING:
            return {
                'success': False,
                'message': f'Code "{code}" ບໍ່ຖືກຕ້ອງ. ກະລຸນາໃຊ້: ci, ct, ce, cl, clc, ctt',
                'updated_count': 0,
                'saved_count': 0
            }
        
        master_enterprise = master_pair.get('com_enterprise_code')
        master_lcic = master_pair.get('LCIC_code')
        
        if not master_enterprise or not master_lcic:
            return {
                'success': False,
                'message': 'ກະລຸນາລະບຸ com_enterprise_code ແລະ LCIC_code ຂອງຄູ່ຫຼັກ',
                'updated_count': 0,
                'saved_count': 0
            }
        
        # ສ້າງ Q objects ສຳລັບຊອກຫາທຸກຄູ່ທີ່ຕ້ອງການອັບເດດ
        query_conditions = Q()
        for pair in mapping_pairs:
            enterprise_code = pair.get('com_enterprise_code')
            lcic_code = pair.get('LCIC_code')
            
            if enterprise_code and lcic_code:
                query_conditions |= Q(
                    com_enterprise_code=enterprise_code,
                    LCIC_code=lcic_code
                )
        
        # ຍົກເວັ້ນຄູ່ຫຼັກ (ບໍ່ຕ້ອງອັບເດດຕົວມັນເອງ)
        query_conditions &= ~Q(
            com_enterprise_code=master_enterprise,
            LCIC_code=master_lcic
        )
        
        # ດຶງຂໍ້ມູນທີ່ຕ້ອງອັບເດດ
        records_to_update = CompanyInfoMapping.objects.filter(query_conditions)
        
        updated_count = 0
        saved_count = 0
        updated_records = []
        saved_records = []
        
        # ເລືອກ Model ທີ່ຈະບັນທຶກຕາມ code
        TargetModel = CompanyMappingService.CODE_MODEL_MAPPING[code]
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # ອັບເດດແຕ່ລະ record
        for record in records_to_update:
            old_enterprise = record.com_enterprise_code
            old_lcic = record.LCIC_code
            
            # ສ້າງຂໍ້ມູນສຳລັບບັນທຶກໃນຕາຕະລາງເປົ້າໝາຍ
            record_data = {
                'segment': record.segment,
                'mm_com_sys_id': record.mm_com_sys_id,
                'bnk_code': record.bnk_code,
                'branchcode': record.branchcode,
                'customerid': record.customerid,
                'com_enterprise_code': old_enterprise,  # ເກັບຄ່າເກົ່າ
                'com_registration_date': record.com_registration_date,
                'com_registration_place_issue': record.com_registration_place_issue,
                'com_name': record.com_name,
                'com_lao_name': record.com_lao_name,
                'com_tax_no': record.com_tax_no,
                'com_category': record.com_category,
                'com_regulatory_capital': record.com_regulatory_capital,
                'com_regulatory_capital_unit': record.com_regulatory_capital_unit,
                'com_insert_date': record.com_insert_date,
                'com_update_date': current_datetime,
                'mm_action_date': current_datetime,
                'mm_log': record.mm_log,
                'mm_comment': f'Merged from {old_enterprise}/{old_lcic} to {master_enterprise}/{master_lcic}',
                'mm_by': record.mm_by,
                'blk_sys_id': record.blk_sys_id,
                'mm_status': record.mm_status,
                'is_manual': record.is_manual,
                'com_lao_name_code': record.com_lao_name_code,
                'LCIC_code': old_lcic,  # ເກັບຄ່າເກົ່າ
                'enterprise_code': master_enterprise,  # ເກັບຄ່າໃໝ່
                'status': 'merged',
                'user': user,
                'main_map': f'{master_enterprise}|{master_lcic}',  # ເກັບຄູ່ຫຼັກ
                'status_action': 'updated'
            }
            
            # ບັນທຶກໃນຕາຕະລາງເປົ້າໝາຍ
            try:
                saved_record = TargetModel.objects.create(**record_data)
                saved_count += 1
                saved_records.append({
                    'target_table': TargetModel.__name__,
                    'saved_id': saved_record.com_sys_id,
                    'old_enterprise_code': old_enterprise,
                    'old_lcic_code': old_lcic,
                    'new_enterprise_code': master_enterprise,
                    'new_lcic_code': master_lcic
                })
            except Exception as e:
                print(f"Error saving to {TargetModel.__name__}: {str(e)}")
            
           
            record.com_enterprise_code = master_enterprise
            record.LCIC_code = master_lcic
            record.com_update_date = current_datetime
            record.save()
            
            updated_count += 1
            updated_records.append({
                'com_sys_id': record.com_sys_id,
                'old_enterprise_code': old_enterprise,
                'old_lcic_code': old_lcic,
                'new_enterprise_code': master_enterprise,
                'new_lcic_code': master_lcic
            })
        
        return {
            'success': True,
            'message': f'ອັບເດດສຳເລັດ {updated_count} records ແລະບັນທຶກ {saved_count} records ໃນ {TargetModel.__name__}',
            'updated_count': updated_count,
            'saved_count': saved_count,
            'target_table': TargetModel.__name__,
            'code': code,
            'master_pair': master_pair,
            'updated_records': updated_records,
            'saved_records': saved_records
        }



def example_usage():
    
   
    mapping_pairs = [
        {'com_enterprise_code': 'ENT001', 'LCIC_code': 'LCIC001'},
        {'com_enterprise_code': 'ENT002', 'LCIC_code': 'LCIC002'},
        {'com_enterprise_code': 'ENT003', 'LCIC_code': 'LCIC003'},
    ]
    
  
    master_pair = {'com_enterprise_code': 'ENT001', 'LCIC_code': 'LCIC001'}
    
    
    result = CompanyMappingService.merge_company_mappings_with_logging(
        mapping_pairs=mapping_pairs,
        master_pair=master_pair,
        code='ci',
        user='admin'
    )
    print(result)
    
   
    result = CompanyMappingService.merge_company_mappings_with_logging(
        mapping_pairs=mapping_pairs,
        master_pair=master_pair,
        code='ct',
        user='admin'
    )
    
   
    result = CompanyMappingService.merge_company_mappings_with_logging(
        mapping_pairs=mapping_pairs,
        master_pair=master_pair,
        code='ce',
        user='admin'
    )