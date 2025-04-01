from celery import shared_task

@shared_task
def process_large_file(file_path):
   
    pass
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import math
from .models import B1, B1_Monthly, Upload_File, memberInfo, User_Group, SType, Upload_Type, EnterpriseInfo, B_Data_is_damaged, data_edit
from datetime import datetime
from django.utils import timezone
import logging

def human_readable_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

logger = logging.getLogger(__name__)

@csrf_exempt
def upload_files(request):
    if request.method == 'POST':
        try:
            user = request.user
            files = request.FILES.getlist('files')
            warnings = []

            for file in files:
                if file.name.endswith('.json'):
                    data = json.load(file)
                    file_size = file.size
                    file_size_hr = human_readable_size(file.size)

                    upload_file = Upload_File.objects.create(
                        fileName=file.name,
                        fileSize=file_size_hr,
                        path="uploadFiles/" + file.name,
                        insertDate=timezone.now(),
                        updateDate=timezone.now(),
                        period="period_value",
                        status="status_value",
                        status_upload="status_upload_value",
                        FileType="json",
                        MID=user.memberinfo if hasattr(user, 'memberinfo') else None,
                        GID=user.user_group if hasattr(user, 'user_group') else None,
                        SType=user.stype if hasattr(user, 'stype') else None,
                        UType=user.upload_type if hasattr(user, 'upload_type') else None,
                    )

                    for item in data:
                        com_enterprise_code = item.get('com_enterprise_code', '')
                        lcicID = item.get('lcicID', '')

                        # Check EnterpriseInfo
                        enterprise_info = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first()
                        if not enterprise_info:
                            warnings.append(f'EnterpriseInfo with EnterpriseID {com_enterprise_code} not found')
                            lcicID_error_status = 1 if lcicID != '' else 10
                            com_enterprise_code_error_status = 20 if com_enterprise_code != '' else '02'

                            B_Data_is_damaged.objects.create(
                                lcicID=lcicID,
                                period=item.get('period', ''),
                                com_enterprise_code=com_enterprise_code,
                                segmentType=item.get('segmentType', ''),
                                bnk_code=item.get('bnk_code', ''),
                                customer_id=item.get('customer_id', ''),
                                branch_id=item.get('branch_id', ''),
                                lon_sys_id=item.get('lon_sys_id', ''),
                                loan_id=item.get('loan_id', ''),
                                lon_open_date=item.get('lon_open_date', None),
                                lon_exp_date=item.get('lon_exp_date', None),
                                lon_ext_date=item.get('lon_ext_date', None),
                                lon_int_rate=item.get('lon_int_rate', 0),
                                lon_purpose_code=item.get('lon_purpose_code', ''),
                                lon_credit_line=item.get('lon_credit_line', 0),
                                lon_currency_code=item.get('lon_currency_code', ''),
                                lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
                                lon_account_no=item.get('lon_account_no', ''),
                                lon_no_days_slow=item.get('lon_no_days_slow', 0),
                                lon_class=item.get('lon_class', ''),
                                lon_type=item.get('lon_type', ''),
                                lon_term=item.get('lon_term', ''),
                                lon_status=item.get('lon_status', ''),
                                lon_insert_date=item.get('lon_insert_date', None),
                                lon_update_date=item.get('lon_update_date', None),
                                lon_applied_date=item.get('lon_applied_date', None),
                                is_disputed=item.get('is_disputed', 0),
                                lcicID_error=lcicID_error_status,
                                com_enterprise_code_error=com_enterprise_code_error_status,
                            )
                            continue

                        if lcicID != enterprise_info.LCICID:
                            lcicID = enterprise_info.LCICID

                        data_edit.objects.create(
                            lcicID=lcicID,
                            period=item.get('period', ''),
                            com_enterprise_code=com_enterprise_code,
                            segmentType=item.get('segmentType', ''),
                            bnk_code=item.get('bnk_code', ''),
                            customer_id=item.get('customer_id', ''),
                            branch_id=item.get('branch_id', ''),
                            lon_sys_id=item.get('lon_sys_id', ''),
                            loan_id=item.get('loan_id', ''),
                            lon_open_date=item.get('lon_open_date', None),
                            lon_exp_date=item.get('lon_exp_date', None),
                            lon_ext_date=item.get('lon_ext_date', None),
                            lon_int_rate=item.get('lon_int_rate', 0),
                            lon_purpose_code=item.get('lon_purpose_code', ''),
                            lon_credit_line=item.get('lon_credit_line', 0),
                            lon_currency_code=item.get('lon_currency_code', ''),
                            lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
                            lon_account_no=item.get('lon_account_no', ''),
                            lon_no_days_slow=item.get('lon_no_days_slow', 0),
                            lon_class=item.get('lon_class', ''),
                            lon_type=item.get('lon_type', ''),
                            lon_term=item.get('lon_term', ''),
                            lon_status=item.get('lon_status', ''),
                            lon_insert_date=item.get('lon_insert_date', None),
                            lon_update_date=item.get('lon_update_date', None),
                            lon_applied_date=item.get('lon_applied_date', None),
                            is_disputed=item.get('is_disputed', 0),
                        )

                        lon_open_date = timezone.make_aware(datetime.strptime(item.get('lon_open_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_open_date') else None
                        lon_exp_date = timezone.make_aware(datetime.strptime(item.get('lon_exp_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_exp_date') else None
                        lon_ext_date = timezone.make_aware(datetime.strptime(item.get('lon_ext_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_ext_date') else None
                        lon_insert_date = timezone.make_aware(datetime.strptime(item.get('lon_insert_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_insert_date') else None
                        lon_update_date = timezone.make_aware(datetime.strptime(item.get('lon_update_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_update_date') else None
                        lon_applied_date = timezone.make_aware(datetime.strptime(item.get('lon_applied_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_applied_date') else None

                        is_disputed = 1 if item.get('is_disputed', 0) else 0

                        B1_Monthly.objects.create(
                            lcicID=lcicID,
                            com_enterprise_code=item.get('com_enterprise_code'),
                            segmentType=item.get('segmentType'),
                            bnk_code=item.get('bnk_code'),
                            customer_id=item.get('customer_id'),
                            branch_id=item.get('branch_id'),
                            lon_sys_id=item.get('lon_sys_id'),
                            loan_id=item.get('loan_id'),
                            lon_open_date=lon_open_date,
                            lon_exp_date=lon_exp_date,
                            lon_ext_date=lon_ext_date,
                            lon_int_rate=item.get('lon_int_rate', 0),
                            lon_purpose_code=item.get('lon_purpose_code'),
                            lon_credit_line=item.get('lon_credit_line', 0),
                            lon_currency_code=item.get('lon_currency_code'),
                            lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
                            lon_account_no=item.get('lon_account_no'),
                            lon_no_days_slow=item.get('lon_no_days_slow', 0),
                            lon_class=item.get('lon_class'),
                            lon_type=item.get('lon_type'),
                            lon_term=item.get('lon_term'),
                            lon_status=item.get('lon_status'),
                            lon_insert_date=lon_insert_date,
                            lon_update_date=lon_update_date,
                            lon_applied_date=lon_applied_date,
                            is_disputed=is_disputed,
                        )

                        existing_b1 = B1.objects.filter(
                            bnk_code=item.get('bnk_code'),
                            branch_id=item.get('branch_id'),
                            customer_id=item.get('customer_id'),
                            loan_id=item.get('loan_id')
                        ).first()

                        if existing_b1:
                            existing_b1.lcicID = lcicID
                            existing_b1.com_enterprise_code = item.get('com_enterprise_code')
                            existing_b1.segmentType = item.get('segmentType')
                            existing_b1.bnk_code = item.get('bnk_code')
                            existing_b1.customer_id = item.get('customer_id')
                            existing_b1.branch_id = item.get('branch_id')
                            existing_b1.lon_sys_id = item.get('lon_sys_id')
                            existing_b1.loan_id = item.get('loan_id')
                            existing_b1.lon_open_date = lon_open_date
                            existing_b1.lon_exp_date = lon_exp_date
                            existing_b1.lon_ext_date = lon_ext_date
                            existing_b1.lon_int_rate = item.get('lon_int_rate', 0)
                            existing_b1.lon_purpose_code = item.get('lon_purpose_code')
                            existing_b1.lon_credit_line = item.get('lon_credit_line', 0)
                            existing_b1.lon_currency_code = item.get('lon_currency_code')
                            existing_b1.lon_outstanding_balance = item.get('lon_outstanding_balance', 0)
                            existing_b1.lon_account_no = item.get('lon_account_no')
                            existing_b1.lon_no_days_slow = item.get('lon_no_days_slow', 0)
                            existing_b1.lon_class = item.get('lon_class')
                            existing_b1.lon_type = item.get('lon_type')
                            existing_b1.lon_term = item.get('lon_term')
                            existing_b1.lon_status = item.get('lon_status')
                            existing_b1.lon_insert_date = lon_insert_date
                            existing_b1.lon_update_date = lon_update_date
                            existing_b1.lon_applied_date = lon_applied_date
                            existing_b1.is_disputed = is_disputed
                            existing_b1.save()
                        else:
                            B1.objects.create(
                                lcicID=lcicID,
                                com_enterprise_code=item.get('com_enterprise_code'),
                                segmentType=item.get('segmentType'),
                                bnk_code=item.get('bnk_code'),
                                customer_id=item.get('customer_id'),
                                branch_id=item.get('branch_id'),
                                lon_sys_id=item.get('lon_sys_id'),
                                loan_id=item.get('loan_id'),
                                lon_open_date=lon_open_date,
                                lon_exp_date=lon_exp_date,
                                lon_ext_date=lon_ext_date,
                                lon_int_rate=item.get('lon_int_rate', 0),
                                lon_purpose_code=item.get('lon_purpose_code'),
                                lon_credit_line=item.get('lon_credit_line', 0),
                                lon_currency_code=item.get('lon_currency_code'),
                                lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
                                lon_account_no=item.get('lon_account_no'),
                                lon_no_days_slow=item.get('lon_no_days_slow', 0),
                                lon_class=item.get('lon_class'),
                                lon_type=item.get('lon_type'),
                                lon_term=item.get('lon_term'),
                                lon_status=item.get('lon_status'),
                                lon_insert_date=lon_insert_date,
                                lon_update_date=lon_update_date,
                                lon_applied_date=lon_applied_date,
                                is_disputed=is_disputed,
                            )
            return JsonResponse({'status': 'success', 'warnings': warnings})
        except Exception as e:
            logger.exception("Failed to upload files")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
    os.remove(file_path)
    
import json
import os
from django.conf import settings
from celery import shared_task
from django.db import transaction
from utility.models import JsonfileWater, UploadJsonFiles,Utility_Bill, FileDetail
def truncate(value, max_length):
    """Truncate string values to fit max_length."""
    return str(value)[:max_length] if value else ''

@shared_task
def process_json_file_task(file_id):
    try:
        file = FileDetail.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, file.file_path.name)
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        records = data.get('message', [])
        total_items = len(records)
        processed_items = file.processed_items

        batch = []
        for item in records[processed_items:]:
            if not Utility_Bill.objects.filter(Payment_ID=item.get('PAYMENT_ID', '')).exists():
                batch.append(Utility_Bill(
                    Customer_ID=truncate(item.get('CUSTOMER_ID', ''), 100),
                    InvoiceNo=truncate(item.get('PAYMENT_ID', ''), 100),
                    TypeOfPro=truncate(item.get('SUPPLY_TYPE', ''), 100),
                    Outstanding=item.get('OUTSTANDING', 0.00),
                    Basic_Tax=item.get('BASIC+TAX', 0.00),
                    Bill_Amount=item.get('BILL_AMOUNT', 0.00),
                    Debt_Amount=0.00,
                    Payment_ID=truncate(item.get('PAYMENT_ID', ''), 255),
                    PaymentType=truncate(item.get('PAY_TYPE', ''), 255),
                    Payment_Date=truncate(item.get('PAYMENT_DATE', ''), 255),
                    InvoiceMonth=truncate(item.get('BILL_OF_MONTH', ''), 50),
                    InvoiceDate=truncate(item.get('DATE_OF_ISSUE', ''), 100),
                    DisID=truncate(item.get('DIS_ID', ''), 100),
                    ProID=truncate(item.get('PRO_ID', ''), 100),
                    UserID=None
                ))
                processed_items += 1
                if len(batch) >= 1000:  # Bulk create every 1000 records
                    Utility_Bill.objects.bulk_create(batch)
                    file.processed_items = processed_items
                    file.save()
                    print(f"Processed {processed_items}/{total_items}")
                    batch = []
        
        if batch:  # Process remaining records
            Utility_Bill.objects.bulk_create(batch)
            file.processed_items = processed_items
            file.save()
            print(f"Processed {processed_items}/{total_items}")
    except Exception as e:
        print(f"Error in Celery task for file {file_id}: {str(e)}")
from celery import Celery, states
from celery.exceptions import Ignore
from .models import Upload_File
import json

app = Celery('lcicHome')

@app.task(bind=True)
def process_uploaded_file(self, file_content: str, file_id: int, user_id: str, period: int):
    try:
        file_data = json.loads(file_content)
        total_items = len(file_data) if isinstance(file_data, list) else 1
        processed_items = 0

        for item in file_data if isinstance(file_data, list) else [file_data]:
            # ປະມວນຜົນແຕ່ລະ item (ຕາມ logic ຂອງເຈົ້າ)
            processed_items += 1
            progress = (processed_items / total_items) * 100
            self.update_state(state='PROGRESS', meta={'progress': progress, 'file_id': file_id})

        Upload_File.objects.filter(FID=file_id).update(statussubmit='1')
    except Exception as e:
        self.update_state(state=states.FAILURE, meta={'error': str(e)})
        raise Ignore()