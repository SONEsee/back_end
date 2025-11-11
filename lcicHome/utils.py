from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    """
    Generate JWT tokens for a custom user model (LCICSystemUser).
    """
    refresh = RefreshToken()
    
 
    refresh['user_id'] = user.id  
    
    
    refresh['username'] = user.username
    refresh['roles'] = user.roles
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
# API Edl Tracking:
# utils.py - Data validation and processing utilities

from decimal import Decimal, InvalidOperation
from datetime import datetime
import re
from django.core.exceptions import ValidationError

class ElectricBillValidator:
    """Utility class for validating electric bill data"""
    
    REQUIRED_FIELDS = [
        'MASTER_BILL_ID', 'INDEX_NO', 'PROVINCE_CODE', 'DIS_ID'
    ]
    
    NUMERIC_FIELDS = [
        'OUTSTANDING', 'BILL_AMOUNT', 'FACT_TOTAL'
    ]
    
    DATE_PATTERN = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    MONTH_PATTERN = re.compile(r'^\d{2}-\d{4}$')
    
    @classmethod
    def validate_record(cls, record, expected_province=None, expected_district=None):
        """
        Validate a single electric bill record
        
        Args:
            record: Dictionary containing electric bill data
            expected_province: Expected province code for validation
            expected_district: Expected district code for validation
            
        Returns:
            dict: {
                'is_valid': bool,
                'errors': list of error messages,
                'warnings': list of warning messages
            }
        """
        errors = []
        warnings = []
        
        # Check required fields
        for field in cls.REQUIRED_FIELDS:
            if not record.get(field):
                errors.append(f"Missing required field: {field}")
        
        # Validate numeric fields
        for field in cls.NUMERIC_FIELDS:
            value = record.get(field)
            if value is not None:
                try:
                    decimal_value = Decimal(str(value))
                    if decimal_value < 0:
                        warnings.append(f"Negative value in {field}: {value}")
                except (InvalidOperation, ValueError, TypeError):
                    errors.append(f"Invalid numeric value in {field}: {value}")
        
        # Validate province and district codes
        if expected_province and record.get('PROVINCE_CODE') != expected_province:
            errors.append(
                f"Province code mismatch: expected {expected_province}, "
                f"got {record.get('PROVINCE_CODE')}"
            )
        
        if expected_district and record.get('DIS_ID') != expected_district:
            errors.append(
                f"District code mismatch: expected {expected_district}, "
                f"got {record.get('DIS_ID')}"
            )
        
        # Validate date formats
        payment_date = record.get('PAYMENTDAY')
        if payment_date and not cls.DATE_PATTERN.match(str(payment_date)):
            warnings.append(f"Invalid payment date format: {payment_date}")
        
        invoice_date = record.get('INVD')
        if invoice_date and not cls.DATE_PATTERN.match(str(invoice_date)):
            warnings.append(f"Invalid invoice date format: {invoice_date}")
        
        invoice_month = record.get('INVM')
        if invoice_month and not cls.MONTH_PATTERN.match(str(invoice_month)):
            warnings.append(f"Invalid invoice month format: {invoice_month}")
        
        # Validate IDs
        customer_id = record.get('MASTER_BILL_ID')
        if customer_id and len(str(customer_id)) > 255:
            errors.append(f"Customer ID too long: {len(str(customer_id))} characters")
        
        payment_id = record.get('PAYMENT_ID')
        if not payment_id:
            warnings.append("Missing Payment ID")
        
        return {
            'is_valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    @classmethod
    def clean_record(cls, record):
        """
        Clean and normalize record da
        
        Args:
            record: Raw record dictionary
            
        Returns:
            dict: Cleaned record dictionary
        """
        cleaned = {}
        
        # Clean string fields
        string_fields = [
            'MASTER_BILL_ID', 'INDEX_NO', 'SUPPLY_TYPE', 'PAYMENT_ID',
            'PAYMENT_WAY', 'PAYMENTDAY', 'INVM', 'INVD', 'DIS_ID', 'PROVINCE_CODE'
        ]
        
        for field in string_fields:
            value = record.get(field, '')
            cleaned[field] = str(value).strip() if value is not None else ''
        
        # Clean numeric fields
        for field in cls.NUMERIC_FIELDS:
            value = record.get(field, 0)
            try:
                cleaned[field] = Decimal(str(value)) if value else Decimal('0.00')
            except (InvalidOperation, ValueError, TypeError):
                cleaned[field] = Decimal('0.00')
        
        return cleaned


class DataProcessingStats:
    """Utility class for tracking data processing statistics"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset all counters"""
        self.total_records = 0
        self.processed_records = 0
        self.failed_records = 0
        self.duplicate_records = 0
        self.validation_errors = []
        self.processing_start_time = None
        self.processing_end_time = None
    
    def start_processing(self):
        """Mark the start of processing"""
        self.processing_start_time = datetime.now()
        self.reset()
    
    def end_processing(self):
        """Mark the end of processing"""
        self.processing_end_time = datetime.now()
    
    def add_record(self, success=True, is_duplicate=False, errors=None):
        """
        Add a record to the statistics
        
        Args:
            success: Whether the record was processed successfully
            is_duplicate: Whether the record was a duplicate
            errors: List of validation errors (if any)
        """
        self.total_records += 1
        
        if is_duplicate:
            self.duplicate_records += 1
        elif success:
            self.processed_records += 1
        else:
            self.failed_records += 1
            if errors:
                self.validation_errors.extend(errors)
    
    @property
    def success_rate(self):
        """Calculate success rate percentage"""
        if self.total_records == 0:
            return 0
        return (self.processed_records / self.total_records) * 100
    
    @property
    def processing_duration(self):
        """Get processing duration in seconds"""
        if self.processing_start_time and self.processing_end_time:
            return (self.processing_end_time - self.processing_start_time).total_seconds()
        return None
    
    @property
    def records_per_second(self):
        """Calculate records processed per second"""
        duration = self.processing_duration
        if duration and duration > 0:
            return self.total_records / duration
        return None
    
    def get_summary(self):
        """Get a summary of processing statistics"""
        return {
            'total_records': self.total_records,
            'processed_records': self.processed_records,
            'failed_records': self.failed_records,
            'duplicate_records': self.duplicate_records,
            'success_rate': round(self.success_rate, 2),
            'processing_duration': self.processing_duration,
            'records_per_second': round(self.records_per_second, 2) if self.records_per_second else None,
            'total_errors': len(self.validation_errors)
        }


def batch_process_electric_bills(records, tracking, username, batch_size=1000):
    """
    Enhanced batch processing with detailed statistics and validation
    
    Args:
        records: List of electric bill records
        tracking: UploadDataTracking instance
        username: Username for the UserID field
        batch_size: Number of records to process in each batch
        
    Returns:
        dict: Processing results with detailed statistics
    """
    from utility.models import Electric_Bill
    from django.db import transaction
    
    stats = DataProcessingStats()
    stats.start_processing()
    validator = ElectricBillValidator()
    
    batch = []
    
    try:
        with transaction.atomic():
            for i, record in enumerate(records, 1):
                # Validate record
                validation_result = validator.validate_record(
                    record, 
                    expected_province=tracking.pro_id,
                    expected_district=tracking.dis_id
                )
                
                if not validation_result['is_valid']:
                    stats.add_record(success=False, errors=validation_result['errors'])
                    continue
                
                # Clean record data
                cleaned_record = validator.clean_record(record)
                
                # Check for duplicates
                if Electric_Bill.objects.filter(
                    Payment_ID=cleaned_record['PAYMENT_ID'],
                    InvoiceNo=cleaned_record['INDEX_NO'][:255],
                    ProID=tracking.pro_id,
                    DisID=tracking.dis_id
                ).exists():
                    stats.add_record(success=False, is_duplicate=True)
                    continue
                
                # Create Electric_Bill object
                bill = Electric_Bill(
                    Customer_ID=cleaned_record['MASTER_BILL_ID'][:255],
                    InvoiceNo=cleaned_record['INDEX_NO'][:255],
                    TypeOfPro=cleaned_record['SUPPLY_TYPE'][:100],
                    Outstanding=cleaned_record['OUTSTANDING'],
                    Basic_Tax=cleaned_record['FACT_TOTAL'],
                    Bill_Amount=cleaned_record['BILL_AMOUNT'],
                    Debt_Amount=Decimal('0.00'),
                    Payment_ID=cleaned_record['PAYMENT_ID'],
                    PaymentType=cleaned_record['PAYMENT_WAY'],
                    Payment_Date=cleaned_record['PAYMENTDAY'],
                    InvoiceMonth=cleaned_record['INVM'][:50],
                    InvoiceDate=cleaned_record['INVD'][:100],
                    DisID=cleaned_record['DIS_ID'][:100],
                    ProID=cleaned_record['PROVINCE_CODE'][:100],
                    UserID=username
                )
                
                batch.append(bill)
                
                # Process batch when it reaches batch_size
                if len(batch) >= batch_size:
                    Electric_Bill.objects.bulk_create(batch, ignore_conflicts=True)
                    
                    for _ in batch:
                        stats.add_record(success=True)
                    
                    # Update tracking
                    tracking.processed_records = stats.processed_records
                    tracking.failed_records = stats.failed_records
                    tracking.save()
                    
                    batch = []
            
            # Process remaining batch
            if batch:
                Electric_Bill.objects.bulk_create(batch, ignore_conflicts=True)
                for _ in batch:
                    stats.add_record(success=True)
        
        stats.end_processing()
        
        # Final tracking update
        tracking.processed_records = stats.processed_records
        tracking.failed_records = stats.failed_records
        tracking.total_records = stats.total_records
        tracking.save()
        
        return {
            'success': True,
            'statistics': stats.get_summary(),
            'message': f'Processing completed: {stats.processed_records}/{stats.total_records} records processed'
        }
        
    except Exception as e:
        stats.end_processing()
        return {
            'success': False,
            'statistics': stats.get_summary(),
            'error': str(e)
        }
    

from datetime import datetime

# === Helper functions ===
def safe_float(value, default=0.0):
    if value in (None, '', 'null'):
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def safe_int(value, default=0):
    if value in (None, '', 'null'):
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def parse_date(date_str):
    if not date_str or date_str in (None, "null", ""):
        return None
    if isinstance(date_str, datetime):
        return date_str.date()
    try:
        return datetime.strptime(str(date_str).split('T')[0].split()[0], "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None

def parse_datetime(dt_str):
    if not dt_str or dt_str in (None, "null", ""):
        return None
    if isinstance(dt_str, datetime):
        return dt_str
    try:
        dt = str(dt_str).split('.')[0] 
        if ' ' in dt:
            return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        else:
            return datetime.strptime(dt.split('T')[0], "%Y-%m-%d")
    except (ValueError, TypeError):
        return None
    

import re
from django.utils import timezone
from .models import data_edit, B_Data_is_damaged, disputes, Upload_File_Individual,CDL,Upload_File_Individual_Collateral


def reject_individual_loan(id_file):
    deleted_count = {
        'data_edit': 0,
        'B_Data_is_damaged': 0,
        'disputes': 0
    }
    fid_to_update = None
    update_status_success = False
    current_status = None

    try:
     
        match = re.match(r'n-(\d+)', id_file.strip())
        if not match:
            return {
                'success': False,
                'message': f'id_file ບໍ່ຖືກຕ້ອງ: {id_file}',
                'details': {}
            }
        fid_to_update = int(match.group(1))

       
        deleted_count['data_edit'] = data_edit.objects.filter(id_file=id_file).delete()[0]
        deleted_count['B_Data_is_damaged'] = B_Data_is_damaged.objects.filter(id_file=id_file).delete()[0]
        deleted_count['disputes'] = disputes.objects.filter(id_file=id_file).delete()[0]
        total_deleted = sum(deleted_count.values())

       
        file_obj = Upload_File_Individual.objects.filter(FID=fid_to_update).first()
        if not file_obj:
            return {
                'success': False,
                'message': f'ບໍ່ພົບຂໍ້ມູນໄຟລ໌ FID: {fid_to_update}',
                'details': {'fid': fid_to_update}
            }

        current_status = file_obj.statussubmit

       
        file_obj.statussubmit = '7'
        file_obj.updateDate = timezone.now()
        file_obj.save()
        update_status_success = True

        
        msg = []
        if total_deleted:
            msg.append(f'ລົບ: {total_deleted} ລາຍການ')
        else:
            msg.append('ບໍ່ມີຂໍ້ມູນຖືກລົບ')

        msg.append(f'ປະຕິເສດສຳເລັດ (FID: {fid_to_update}) → statussubmit {current_status} → 7')

        return {
            'success': True,
            'message': ' | '.join(msg),
            'details': {
                'id_file': id_file,
                'fid': fid_to_update,
                'current_status': current_status,
                'new_status': '7',
                'deleted': deleted_count,
                'status_updated': update_status_success
            }
        }

    except Exception as e:
        return {
            'success': False,
            'message': f'ເກີດຂໍ້ຜິດພາດ: {str(e)}',
            'details': {
                'id_file': id_file,
                'fid_extracted': fid_to_update,
                'current_status': current_status,
                'deleted': deleted_count
            }
        }
    
def reject_individual_collateral(id_file):
    deleted_count = {
        'CDL': 0,
        
    }
    cid_to_update = None
    update_status_success = False
    current_status = None

    try:
     
        match = re.match(r'c-(\d+)', id_file.strip())
        if not match:
            return {
                'success': False,
                'message': f'id_file ບໍ່ຖືກຕ້ອງ: {id_file}',
                'details': {}
            }
        cid_to_update = int(match.group(1))

       
        deleted_count['CDL'] = data_edit.objects.filter(id_file=id_file).delete()[0]
       
        total_deleted = sum(deleted_count.values())

       
        file_obj = Upload_File_Individual_Collateral.objects.filter(CID=cid_to_update).first()
        if not file_obj:
            return {
                'success': False,
                'message': f'ບໍ່ພົບຂໍ້ມູນໄຟລ໌ FID: {cid_to_update}',
                'details': {'fid': cid_to_update}
            }

        current_status = file_obj.statussubmit

       
        file_obj.statussubmit = '7'
        file_obj.updateDate = timezone.now()
        file_obj.save()
        update_status_success = True

        
        msg = []
        if total_deleted:
            msg.append(f'ລົບ: {total_deleted} ລາຍການ')
        else:
            msg.append('ບໍ່ມີຂໍ້ມູນຖືກລົບ')

        msg.append(f'ປະຕິເສດສຳເລັດ (FID: {cid_to_update}) → statussubmit {current_status} → 7')

        return {
            'success': True,
            'message': ' | '.join(msg),
            'details': {
                'id_file': id_file,
                'fid': cid_to_update,
                'current_status': current_status,
                'new_status': '7',
                'deleted': deleted_count,
                'status_updated': update_status_success
            }
        }

    except Exception as e:
        return {
            'success': False,
            'message': f'ເກີດຂໍ້ຜິດພາດ: {str(e)}',
            'details': {
                'id_file': id_file,
                'fid_extracted': cid_to_update,
                'current_status': current_status,
                'deleted': deleted_count
            }
        }
    

# utils.py
from django.db import transaction
from django.utils import timezone
from .models import (
    Upload_File_Individual_Collateral, CDL, C1,
    col_real_estates, col_money_mia, col_equipment_eqi,
    col_project_prj, col_vechicle_veh, col_guarantor_gua,
    col_goldsilver_gold, col_guarantor_com
)

# ກຳນົດກ່ອນຟັງຊັນ
COLLATERAL_MODELS = {
    'c2.1': col_real_estates,
    'c2.2': col_money_mia,
    'c2.3': col_equipment_eqi,
    'c2.4': col_project_prj,
    'c2.5': col_vechicle_veh,
    'c2.6': col_guarantor_gua,
    'c2.7': col_goldsilver_gold,
    'c2.8': col_guarantor_com,
}

def confirm_collateral_logic(CID_with_prefix):
    print(f"\n{'='*80}")
    print(f"START: confirm_collateral_logic - CID: {CID_with_prefix}")
    print(f"{'='*80}")
    start_time = timezone.now()
    CID_number = None

    try:
        # 1. ກວດ CID
        if CID_with_prefix.startswith('c-'):
            CID_number = int(CID_with_prefix.replace('c-', ''))
        else:
            CID_number = int(CID_with_prefix)
        
        print(f"  CID_number: {CID_number}")

        # 2. ກວດໄຟລ໌
        upload_file = Upload_File_Individual_Collateral.objects.filter(CID=CID_number).first()
        if not upload_file:
            print(f"  ❌ ບໍ່ພົບໄຟລ໌ CID={CID_number}")
            return {'status': 'error', 'message': 'ບໍ່ພົບໄຟລ໌ Collateral', 'code': 404}

        print(f"  ພົບໄຟລ໌: statussubmit={upload_file.statussubmit}")

        if upload_file.statussubmit == '0':
            return {'status': 'error', 'message': 'ໄຟລ໌ຖືກຢືນຢັນແລ້ວ', 'code': 400}
        if upload_file.statussubmit == '2':
            return {'status': 'error', 'message': 'ການຢືນຢັນຜິດພາດກ່ອນໜ້າ', 'code': 400}

        # ອັບເດດ → ກຳລັງປະມວນຜົນ
        Upload_File_Individual_Collateral.objects.filter(CID=CID_number).update(statussubmit='3')
        print("  ອັບເດດ statussubmit → '3' (ກຳລັງປະມວນຜົນ)")

        # 3. ດຶງ CDL
        print(f"  ກຳລັງດຶງຂໍ້ມູນຈາກ CDL ທີ່ມີ id_file='{CID_with_prefix}'...")
        cdl_count = CDL.objects.filter(id_file=CID_with_prefix).count()
        print(f"  ມີ CDL ທັງໝົດ: {cdl_count} ແຖວ")
        
        if cdl_count == 0:
            Upload_File_Individual_Collateral.objects.filter(CID=CID_number).update(statussubmit='2')
            return {'status': 'error', 'message': f'ບໍ່ພົບຂໍ້ມູນໃນ CDL ສຳລັບ id_file={CID_with_prefix}', 'code': 404}

        data_list = list(CDL.objects.filter(id_file=CID_with_prefix).values(
            'id_file', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10',
            'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20',
            'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30',
            'c31', 'c32', 'c33', 'c34', 'c35', 'c36', 'c37', 'c39',
            'period', 'col_type', 'user_id'
        ))

        print(f"  ພົບ {len(data_list)} ລາຍການ")

        # ... ສ່ວນທີ່ເຫຼືອຂອງ function ຍັງຄືເກົ່າ

        # 4. ກວດ period
        first_item = data_list[0]
        current_period = first_item['period']
        bnk_code = first_item['c3']
        segment_type = first_item['c39'] or ''

        print(f"  ກວດ period: {current_period}, bnk_code: {bnk_code}, segmentType: '{segment_type}'")

        latest_c1 = C1.objects.filter(
            bnk_code=bnk_code,
            segmentType=segment_type
        ).order_by('-period').first()

        if latest_c1 and int(current_period) < int(latest_c1.period):
            Upload_File_Individual_Collateral.objects.filter(CID=CID_number).update(statussubmit='2')
            return {
                'status': 'error',
                'message': f'Period {current_period} ໜ້ອຍກວ່າ C1 ຫຼ້າສຸດ {latest_c1.period}',
                'code': 400
            }

        # 5. ສ້າງ keys
        print("  ກຳລັງສ້າງ keys ສຳລັບການກວດຊ້ຳ...")
        c1_keys = set()
        col_keys_by_type = {k: set() for k in COLLATERAL_MODELS.keys()}

        for item in data_list:
            if not all([item['c1'], item['c2'], item['c3'], item['c4'], item['c5'], item['c6'], item['c7'], item['period']]):
                continue
            c1_keys.add((item['c1'], item['c3'], item['c6'], item['c7']))
            col_type = (item['col_type'] or '').lower()
            if col_type in col_keys_by_type:
                col_keys_by_type[col_type].add((item['c1'], item['c3'], item['c6'], item['c7'], item['period']))

        # 6. ດຶງ existing data
        print("  ກຳລັງດຶງຂໍ້ມູນທີ່ມີຢູ່ແລ້ວ...")
        existing_c1 = {}
        if c1_keys:
            for r in C1.objects.filter(bnk_code=bnk_code).values('id', 'LCIC_code', 'bnk_code', 'loan_id', 'col_id').iterator():
                key = (r['LCIC_code'], r['bnk_code'], r['loan_id'], r['col_id'])
                if key in c1_keys:
                    existing_c1[key] = r['id']

        existing_by_type = {}
        for col_type, keys in col_keys_by_type.items():
            if not keys:
                continue
            model = COLLATERAL_MODELS[col_type]
            existing_by_type[col_type] = {}
            for r in model.objects.filter(bnk_code=bnk_code, period=current_period).values(
                'id', 'LCIC_code', 'bnk_code', 'loan_id', 'col_id', 'period'
            ).iterator():
                key = (r['LCIC_code'], r['bnk_code'], r['loan_id'], r['col_id'], r['period'])
                if key in keys:
                    existing_by_type[col_type][key] = r['id']

        # 7. ສ້າງ objects ໃໝ່
        print("  ກຳລັງສ້າງ objects ໃໝ່...")
        batch_size = 2000
        c1_objects = []
        col_objects = {k: [] for k in COLLATERAL_MODELS.keys()}
        delete_ids = {'c1': set(), **{k: set() for k in COLLATERAL_MODELS.keys()}}
        now = timezone.now()

        for item in data_list:
            if not all([item['c1'], item['c2'], item['c3'], item['c4'], item['c5'], item['c6'], item['c7'], item['period']]):
                continue

            # === C1 ===
            c1_key = (item['c1'], item['c3'], item['c6'], item['c7'])
            if c1_key in existing_c1:
                delete_ids['c1'].add(existing_c1[c1_key])

            c1_objects.append(C1(
                LCIC_code=item['c1'],
                com_enterprise_code=item['c2'],
                bnk_code=item['c3'],
                bank_customer_ID=item['c4'],
                branch_id_code=item['c5'],
                loan_id=item['c6'],
                col_id=item['c7'],
                segmentType=item['c39'],
                user_id=item['user_id'],
                period=item['period'],
                col_type=item['col_type'],
                id_file=item['id_file'],  # ໃຊ້ຈາກ CDL ແທ້ໆ
                insert_date=now,
                update_date=now
            ))

            # === Collateral ===
            col_type = (item['col_type'] or '').lower()
            if col_type not in COLLATERAL_MODELS:
                continue

            col_key = (item['c1'], item['c3'], item['c6'], item['c7'], item['period'])
            if col_key in existing_by_type.get(col_type, {}):
                delete_ids[col_type].add(existing_by_type[col_type][col_key])

            # c2.1 - ທີ່ດິນ
            if col_type == 'c2.1':
                col_objects['c2.1'].append(col_real_estates(
                    LCIC_code=item['c1'], com_enterprise_code=item['c2'], period=item['period'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], col_value=item['c8'], col_type=item['col_type'],
                    plot_vilid=item['c20'], segmentType=item['c39'], plot_unit=item['c21'], land_no=item['c16'],
                    land_out_time=item['c17'], value_unit=item['c11'], land_type=item['c15'], col_area=item['c10'],
                    land_registry_book_no=item['c14'], land_document_no=item['c13'], place_regist_land=item['c19'],
                    land_map_no=item['c12'], land_plot_no=item['c9'], land_regis_date=item['c18'],
                    land_area=item['c10'], land_unit=item['c11'], owner_name=item['c22'], owner_birth_date=item['c23'],
                    owner_nationality=item['c24'], owner_occupation=item['c25'], current_unit=item['c27'],
                    current_vilid=item['c26'], spouse_name=item['c29'], spouse_birth_date=item['c30'],
                    spouse_nationality=item['c31'], spouse_occupation=item['c32'], land_acquisition=item['c33'],
                    ownership_status=item['c28'], user_id=item['user_id'], id_file=item['id_file'],
                    insert_date=now, update_date=now
                ))

            # c2.2 - ເງິນຝາກ
            elif col_type == 'c2.2':
                col_objects['c2.2'].append(col_money_mia(
                    LCIC_code=item['c1'], period=item['period'], com_enterprise_code=item['c2'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], account_no=item['c8'], col_type=item['col_type'],
                    account_type=item['c9'], segmentType=item['c39'], value_unit=item['c11'], value=item['c10'],
                    mia_insert_date=item['c13'], mia_status=item['c12'], owner_gender=item['c16'],
                    owner_name=item['c14'], owner_surname=item['c15'], owner_lao_name=item['c17'],
                    owner_lao_surname=item['c18'], id_file=item['id_file'], insert_date=now, update_date=now,
                    user_id=item['user_id']
                ))

            # c2.3 - ເຄື່ອງຈັກ
            elif col_type == 'c2.3':
                col_objects['c2.3'].append(col_equipment_eqi(
                    LCIC_code=item['c1'], com_enterprise_code=item['c2'], period=item['period'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], machine_type=item['c8'], machine_no=item['c9'],
                    value=item['c10'], value_unit=item['c11'], machine_status=item['c12'],
                    machine_insert_date=item['c13'], owner_name=item['c14'], owner_surname=item['c15'],
                    owner_gender=item['c16'], owner_lao_name=item['c17'], owner_lao_surname=item['c18'],
                    segmentType=item['c39'], user_id=item['user_id'], id_file=item['id_file'], insert_date=now,
                    update_date=now, col_type=item['col_type']
                ))

            # c2.4 - ໂຄງການ
            elif col_type == 'c2.4':
                col_objects['c2.4'].append(col_project_prj(
                    LCIC_code=item['c1'], com_enterprise_code=item['c2'], period=item['period'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], ministry=item['c8'], project_name_en=item['c9'],
                    project_name_la=item['c10'], project_number=item['c11'], value=item['c12'],
                    value_unit=item['c13'], project_status=item['c14'], project_insert_date=item['c15'],
                    owner_name=item['c16'], owner_surname=item['c17'], owner_gender=item['c18'],
                    owner_lao_name=item['c19'], owner_lao_surname=item['c20'], segmentType=item['c39'],
                    user_id=item['user_id'], id_file=item['id_file'], insert_date=now, update_date=now,
                    col_type=item['col_type']
                ))

            # c2.5 - ຍານພາຫະນະ
            elif col_type == 'c2.5':
                col_objects['c2.5'].append(col_vechicle_veh(
                    LCIC_code=item['c1'], com_enterprise_code=item['c2'], period=item['period'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], plate_number=item['c8'], engine_number=item['c9'],
                    body_number=item['c10'], model=item['c11'], value=item['c12'], value_unit=item['c13'],
                    vehicle_status=item['c14'], vehicle_insert_date=item['c15'], owner_name=item['c16'],
                    owner_surname=item['c17'], owner_gender=item['c18'], owner_lao_name=item['c19'],
                    owner_lao_surname=item['c20'], segmentType=item['c39'], user_id=item['user_id'],
                    id_file=item['id_file'], insert_date=now, update_date=now, col_type=item['col_type']
                ))

            
            elif col_type == 'c2.6':
                col_objects['c2.6'].append(col_guarantor_gua(
                    LCIC_code=item['c1'], com_enterprise_code=item['c2'], period=item['period'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], value=item['c8'], value_unit=item['c9'],
                    gua_ind_status=item['c10'], gua_ind_insert_date=item['c11'], guarantor_nationality=item['c12'],
                    gua_national_id=item['c13'], national_id_expiry_date=item['c14'], gua_passport=item['c15'],
                    passport_expiry_date=item['c16'], gua_familybook_id=item['c17'], familybook_provision_code=item['c18'],
                    familybook_issue_date=item['c19'], gua_birthday=item['c20'], gua_gender=item['c21'],
                    gua_name=item['c22'], gua_surname=item['c23'], gua_lao_name=item['c24'], gua_lao_surname=item['c25'],
                    address_number_street_eng=item['c26'], address_vill_eng=item['c27'], address_district_eng=item['c28'],
                    address_number_street_la=item['c29'], address_vill_la=item['c30'], address_district_la=item['c31'],
                    address_province_code=item['c32'], owner_name=item['c33'], owner_surname=item['c34'],
                    owner_gender=item['c35'], owner_lao_name=item['c36'], owner_lao_surname=item['c37'],
                    segmentType=item['c39'], user_id=item['user_id'], id_file=item['id_file'], insert_date=now,
                    update_date=now, col_type=item['col_type']
                ))

            # c2.7 - ຄຳ/ເງິນ
            elif col_type == 'c2.7':
                col_objects['c2.7'].append(col_goldsilver_gold(
                    LCIC_code=item['c1'], com_enterprise_code=item['c2'], period=item['period'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], weight=item['c8'], value=item['c9'],
                    unit=item['c10'], value_unit=item['c11'], gld_status=item['c12'], gld_insert_date=item['c13'],
                    owner_name=item['c14'], owner_surname=item['c15'], owner_gender=item['c16'],
                    owner_lao_name=item['c17'], owner_lao_surname=item['c18'], segmentType=item['c39'],
                    user_id=item['user_id'], id_file=item['id_file'], insert_date=now, update_date=now,
                    col_type=item['col_type']
                ))

           
            elif col_type == 'c2.8':
                col_objects['c2.8'].append(col_guarantor_com(
                    LCIC_code=item['c1'], com_enterprise_code=item['c2'], period=item['period'],
                    bnk_code=item['c3'], bank_customer_ID=item['c4'], branch_id_code=item['c5'],
                    loan_id=item['c6'], col_id=item['c7'], value=item['c8'], value_unit=item['c9'],
                    gua_com_status=item['c10'], gua_com_insert_date=item['c11'], gua_enterprise_code=item['c12'],
                    enterprise_regist_date=item['c13'], enterprise_regist_place=item['c14'], company_name=item['c15'],
                    company_lao_name=item['c16'], enterprise_category=item['c17'], owner_name=item['c18'],
                    owner_surname=item['c19'], owner_gender=item['c20'], owner_lao_name=item['c21'],
                    owner_lao_surname=item['c22'], segmentType=item['c39'], user_id=item['user_id'],
                    id_file=item['id_file'], insert_date=now, update_date=now, col_type=item['col_type']
                ))

        # 8. ບັນທຶກຂໍ້ມູນໃນທຸລະກຳດຽວ
        print("  ກຳລັງບັນທຶກຂໍ້ມູນ...")
        with transaction.atomic():
            # ລຶບເກົ່າ
            if delete_ids['c1']:
                C1.objects.filter(id__in=delete_ids['c1']).delete()
            for col_type, ids in delete_ids.items():
                if col_type != 'c1' and ids:
                    COLLATERAL_MODELS[col_type].objects.filter(id__in=ids).delete()

            # ສ້າງໃໝ່
            if c1_objects:
                C1.objects.bulk_create(c1_objects, batch_size=batch_size)
            for col_type, objs in col_objects.items():
                if objs:
                    COLLATERAL_MODELS[col_type].objects.bulk_create(objs, batch_size=batch_size)

            # ອັບເດດສະຖານະ
            Upload_File_Individual_Collateral.objects.filter(CID=CID_number).update(
                statussubmit='0', dispuste=0, updateDate=timezone.now()
            )

        total_time = (timezone.now() - start_time).total_seconds()
        print(f"{'='*80}")
        print(f"SUCCESS! Total time: {total_time:.2f}s")
        print(f"{'='*80}")

        return {
            'status': 'success',
            'message': 'ຢືນຢັນຂໍ້ມູນສຳເລັດ',
            'stats': {
                'total_records': len(data_list),
                'processing_time': f"{total_time:.2f}s",
                'updated_c1': len(delete_ids['c1']),
                'created_c1': len(c1_objects) - len(delete_ids['c1'])
            }
        }

    except Exception as e:
        print(f"ERROR in confirm_collateral_logic: {str(e)}")
        import traceback
        traceback.print_exc()

        if CID_number is not None:
            try:
                Upload_File_Individual_Collateral.objects.filter(CID=CID_number).update(
                    statussubmit='2', updateDate=timezone.now()
                )
            except:
                pass

        return {'status': 'error', 'message': str(e), 'code': 500}