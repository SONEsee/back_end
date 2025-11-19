#view.py
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import SType, TelecomCustomer, UploadFileTelecom,Telecom_Bill
from .serializers import STypeSerializer, TelecomCustomerSerializer, UploadFileTelecomSerializer,TelecomBillSerializer

class STypeListCreate(generics.ListCreateAPIView):
    queryset = SType.objects.all()
    serializer_class = STypeSerializer  
    
class STypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SType.objects.all()
    serializer_class = STypeSerializer  

class TelecomPagination(PageNumberPagination):
    page_size = 25  # จำนวน record ต่อหน้า
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TelecomCusListCreate(generics.ListCreateAPIView):
    queryset = TelecomCustomer.objects.all()
    serializer_class = TelecomCustomerSerializer
    pagination_class = TelecomPagination

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                'success': True,
                'message': f'ສ້າງຂໍ້ມູນສຳເລັດ {len(serializer.data)} ລາຍການ',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            # ຖ້າເປັນ dict ສ້າງ 1 record
            return super().create(request, *args, **kwargs)

class TelecomCusRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TelecomCustomer.objects.all()
    serializer_class = TelecomCustomerSerializer

class TelecomBillPagination(PageNumberPagination):
    page_size = 25  
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TelecomBillListCreate(generics.ListCreateAPIView):
    queryset = Telecom_Bill.objects.all()
    serializer_class = TelecomBillSerializer
    pagination_class = TelecomBillPagination

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                'success': True,
                'message': f'ສ້າງຂໍ້ມູນສຳເລັດ {len(serializer.data)} ລາຍການ',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            # ຖ້າເປັນ dict ສ້າງ 1 record
            return super().create(request, *args, **kwargs)

class TelecomBillRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Telecom_Bill.objects.all()
    serializer_class = TelecomBillSerializer

import uuid
import json
from django.db import transaction
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class UploadJsonTelecomView(APIView):

    def post(self, request):
        file_obj = request.FILES.get("file")
        if not file_obj:
            return Response({"error": "ກະລຸນາເລືອກໄຟລ໌"}, status=status.HTTP_400_BAD_REQUEST)

        if not file_obj.name.lower().endswith(".json"):
            return Response({"error": "ຮອງແຕ່ .json"}, status=status.HTTP_400_BAD_REQUEST)

        user_id = request.data.get("user_id", "")
        telecomType = request.data.get("telecomType", "")
        period = request.data.get("period", "")

        # สร้าง UploadFileTelecom record เบื้องต้น
        file_id = str(uuid.uuid4())
        upload = UploadFileTelecom.objects.create(
            SType=None,
            user_id=user_id,
            file_id=file_id,
            fileName=file_obj.name,
            fileUpload=file_obj,
            progress_percentage=0,
            telecomType=telecomType,
            fileSize=str(file_obj.size),
            path="",
            period=period,
            status="processing",
            status_upload="uploaded",
            FileType=".json",
            percentage=0.0
        )
        # update path (file saved)
        try:
            upload.path = upload.fileUpload.path
            upload.save(update_fields=['path'])
        except Exception:
            # บาง environment fileUpload.path อาจยังใช้งานไม่ได้ — ไม่เป็นไร ให้เก็บว่างไว้
            pass

        # อ่าน JSON
        try:
            file_obj.seek(0)
            data = json.load(file_obj)
            if not isinstance(data, list):
                data = [data]
        except json.JSONDecodeError as e:
            upload.status = 'failed'
            upload.save(update_fields=['status'])
            return Response({"error": f"JSON decode error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        if len(data) == 0:
            upload.status = 'failed'
            upload.save(update_fields=['status'])
            return Response({"error": "ไฟล์ JSON ว่าง"}, status=status.HTTP_400_BAD_REQUEST)

        # detect type by keys of first item
        first = data[0]
        if "BillID" in first:
            file_type = "bill"
        elif "Customer_ID" in first:
            file_type = "customer"
        else:
            upload.status = 'failed'
            upload.save(update_fields=['status'])
            return Response({"error": "Unknown JSON structure (not customer or bill)"}, status=status.HTTP_400_BAD_REQUEST)

        total = len(data)
        inserted = 0
        updated = 0
        errors = []

        # ใช้ transaction savepoint — ถ้ามี error เราจะ rollback ทั้งหมด
        sid = transaction.savepoint()
        try:
            if file_type == "customer":
                for idx, item in enumerate(data, start=1):

                    def normalize(value):
                        if value in ["null", "NULL", None]:
                            return None
                        if value in ["", " "]:
                            return ""      # return empty string instead of None
                        return value

                    payload = {
                        "No": normalize(item.get("No")),
                        "Customer_ID": normalize(item.get("Customer_ID")),
                        "Company_name": normalize(item.get("Company_Name")) or normalize(item.get("Company_name")),
                        "Name": normalize(item.get("Name")),
                        "Surname": normalize(item.get("Surname")),
                        "National_ID": normalize(item.get("National_ID")),
                        "Passport": normalize(item.get("Passport")),
                        "Address": normalize(item.get("Address")),
                        "Dustrict_ID": normalize(item.get("Dustrict_ID")),
                        "Province_ID": normalize(item.get("Province_ID")),
                        "Tel": normalize(item.get("Tel")),
                        "Email": normalize(item.get("Email")),
                        "Cus_type": normalize(item.get("Cus_type")),
                        "Regis_date": normalize(item.get("Regis_date")) or normalize(item.get("RegisDate")),
                        "InsertDate": normalize(item.get("InsertDate")),
                        "UpdateDate": normalize(item.get("UpdateDate")),
                        "telecomType": telecomType
                    }

                    cust_id = payload.get("Customer_ID")
                    if not cust_id:
                        errors.append({"index": idx, "error": "Missing Customer_ID"})
                        continue

                    # check existing
                    existing = TelecomCustomer.objects.filter(Customer_ID=cust_id).first()

                    if existing:
                        serializer = TelecomCustomerSerializer(existing, data=payload, partial=True)
                    else:
                        serializer = TelecomCustomerSerializer(data=payload)

                    if serializer.is_valid():
                        serializer.save()
                        if existing:
                            updated += 1
                        else:
                            inserted += 1
                    else:
                        errors.append({"index": idx, "Customer_ID": cust_id, "errors": serializer.errors})

            elif file_type == "bill":
                for idx, item in enumerate(data, start=1):
                    payload = {
                        "BillID": item.get("BillID"),
                        "Customer_ID": item.get("Customer_ID", "") or "",
                        "InvoiceNo": item.get("InvoiceNo", "") or "",
                        "TypeOfPro": item.get("TypeOfPro", "") or "",
                        "Outstanding": item.get("Outstanding"),
                        "Basic_Tax": item.get("Basic_Tax"),
                        "Bill_Amount": item.get("Bill_Amount"),
                        "Debt_Amount": item.get("Debt_Amount"),
                        "Payment_ID": item.get("Payment_ID"),
                        "PaymentType": item.get("PaymentType"),
                        "Payment_Date": item.get("Payment_Date"),
                        "InvoiceMonth": item.get("InvoiceMonth"),
                        "InvoiceDate": item.get("InvoiceDate"),
                        "DisID": item.get("DisID"),
                        "ProID": item.get("ProID"),
                        "telecomType": telecomType,
                        "UserID": user_id
                    }

                    bill_id = payload.get("BillID")
                    if bill_id is None:
                        errors.append({"index": idx, "BillID": bill_id, "error": "Missing BillID"})
                        continue

                    try:
                        existing = Telecom_Bill.objects.filter(BillID=bill_id).first()
                        if existing:
                            serializer = TelecomBillSerializer(existing, data=payload, partial=True)
                        else:
                            serializer = TelecomBillSerializer(data=payload)

                        if serializer.is_valid():
                            serializer.save()
                            if existing:
                                updated += 1
                            else:
                                inserted += 1
                        else:
                            errors.append({"index": idx, "BillID": bill_id, "errors": serializer.errors})

                    except Exception as e:
                        errors.append({"index": idx, "BillID": bill_id, "errors": str(e)})

            # ถ้ามี errors -> rollback ทั้งหมด
            if errors:
                transaction.savepoint_rollback(sid)
                upload.status = 'failed'
                upload.save(update_fields=['status'])
                return Response({
                    "file": upload.fileName,
                    "file_type": file_type,
                    "total": total,
                    "inserted": inserted,
                    "updated": updated,
                    "errors_count": len(errors),
                    "errors_sample": errors[:10]
                }, status=status.HTTP_400_BAD_REQUEST)

            # commit
            transaction.savepoint_commit(sid)
            upload.status = 'completed'
            upload.progress_percentage = 100
            upload.percentage = 100.0
            upload.save(update_fields=['status', 'progress_percentage', 'percentage'])

            return Response({
                "file": upload.fileName,
                "file_type": file_type,
                "total": total,
                "inserted": inserted,
                "updated": updated,
                "message": "Upload and import successful"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            # rollback and mark failed
            transaction.savepoint_rollback(sid)
            upload.status = 'failed'
            upload.save(update_fields=['status'])
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class UploadJsonFileView(APIView):
#     def post(self, request):
#         try:
#             # --- ຮັບໄຟລ໌ ---
#             file_obj = request.FILES.get('file')
#             if not file_obj:
#                 return Response({"error": "ກະລຸນາເລືອກໄຟລ໌"}, status=400)
#             if not file_obj.name.lower().endswith('.json'):
#                 return Response({"error": "ຮອງຮັບແຕ່ .json"}, status=400)

#             # --- ຮັບຂໍ້ມູນ ---
#             user_id = request.POST.get('user_id', 'unknown')
#             telecom_type = request.POST.get('telecomType', 'Unknown')
#             period = request.POST.get('period', '')
#             stype_id = request.POST.get('stype_id')

#             # --- ສ້າງ file_id ---
#             file_id = str(uuid.uuid4())

#             # --- ຄຳນວນຂະໜາດ ---
#             size = file_obj.size
#             if size < 1024:
#                 file_size = f"{size} B"
#             elif size < 1024**2:
#                 file_size = f"{size/1024:.1f} KB"
#             elif size < 1024**3:
#                 file_size = f"{size/(1024**2):.1f} MB"
#             else:
#                 file_size = f"{size/(1024**3):.1f} GB"

#             # --- ບັນທຶກໄຟລ໌ລົງ DB ---
#             upload = UploadFileTelecom(
#                 fileUpload=file_obj,
#                 fileName=file_obj.name,
#                 file_id=file_id,
#                 user_id=user_id,
#                 telecomType=telecom_type,
#                 period=period,
#                 status='processing',
#                 status_upload='uploaded',
#                 FileType='.json',
#                 fileSize=file_size,
#                 path='',
#                 progress_percentage=0,
#                 percentage=0.0
#             )
#             if stype_id:
#                 try:
#                     upload.SType = SType.objects.get(id=stype_id)
#                 except SType.DoesNotExist:
#                     pass
#             upload.save()
#             upload.path = upload.fileUpload.path
#             upload.save(update_fields=['path'])

#             # --- ອ່ານ JSON ຈາກໄຟລ໌ ---
#             try:
#                 file_obj.seek(0)  # reset pointer
#                 data = json.load(file_obj)
#                 if not isinstance(data, list):
#                     data = [data]
#             except json.JSONDecodeError as e:
#                 upload.status = 'failed'
#                 upload.save(update_fields=['status'])
#                 return Response({"error": f"ໄຟລ໌ JSON ບໍ່ຖືກຕ້ອງ: {str(e)}"}, status=400)

#             # --- ກຳນົດຟີລດທີ່ໃຊ້ກວດຊ້ຳ ---
#             duplicate_check_fields = ['Customer_ID', 'Tel', 'Dustrict_ID', 'Province_ID', 'Address', 'Passport']

#             # --- ດຶງ Customer_IDs ທີ່ມີຢູ່ໃນ DB ---
#             existing_customers = TelecomCustomer.objects.filter(
#                 Customer_ID__in=[item.get('Customer_ID') for item in data if item.get('Customer_ID')]
#             ).values('Customer_ID', 'Tel', 'Dustrict_ID', 'Province_ID', 'Address', 'Passport')

#             existing_set = {
#                 (
#                     c['Customer_ID'],
#                     c['Tel'],
#                     c['Dustrict_ID'],
#                     c['Province_ID'],
#                     c['Address'],
#                     c['Passport']
#                 ) for c in existing_customers
#             }

#             new_records = []
#             duplicates = []
#             valid_count = 0

#             # --- ກວດຊ້ຳແລະເກັບໃໝ່ ---
#             for item in data:
#                 key = tuple(item.get(field, '') for field in duplicate_check_fields)
#                 if key in existing_set:
#                     duplicates.append(item)
#                     continue

#                 # ກຳນົດ No ອັດຕະໂນມັດ (ເລີ່ມຈາກ 1)
#                 valid_count += 1
#                 new_record = {
#                     'No': str(valid_count),
#                     'Customer_ID': item.get('Customer_ID', ''),
#                     'Company_name': item.get('Company_name', ''),
#                     'Name': item.get('Name', ''),
#                     'Surname': item.get('Surname', ''),
#                     'National_ID': item.get('National_ID', ''),
#                     'Passport': item.get('Passport', ''),
#                     'Address': item.get('Address', ''),
#                     'Dustrict_ID': item.get('Dustrict_ID', ''),
#                     'Province_ID': item.get('Province_ID', ''),
#                     'Tel': item.get('Tel', ''),
#                     'Email': item.get('Email', ''),
#                     'Cus_type': item.get('Cus_type', ''),
#                     'Regis_date': item.get('Regis_date', ''),
#                     'InsertDate': upload.insertDate.strftime('%Y-%m-%d %H:%M:%S'),
#                     'UpdateDate': None
#                 }
#                 new_records.append(TelecomCustomer(**new_record))

#             # --- ບັນທຶກດ້ວຍ Transaction ---
#             try:
#                 with transaction.atomic():
#                     TelecomCustomer.objects.bulk_create(
#                         new_records,
#                         update_conflicts=True,
#                         update_fields=[
#                             'No', 'Company_name', 'Name', 'Surname', 'National_ID',
#                             'Passport', 'Address', 'Dustrict_ID', 'Province_ID',
#                             'Tel', 'Email', 'Cus_type', 'Regis_date', 'InsertDate', 'UpdateDate'
#                         ],
#                         unique_fields=['Customer_ID']
#                     )
#                 upload.status = 'completed'
#                 upload.progress_percentage = 100
#                 upload.percentage = 100.0
#                 upload.save(update_fields=['status', 'progress_percentage', 'percentage'])
#             except Exception as db_error:
#                 upload.status = 'failed'
#                 upload.save(update_fields=['status'])
#                 logger.error(f"DB Error: {str(db_error)}")
#                 return Response({"error": f"ບັນທຶກລົງ DB ບໍ່ສຳເລັດ: {str(db_error)}"}, status=500)

#             # --- ສົ່ງຜົນກັບຄືນ ---
#             return Response({
#                 "message": "ປະມວນຜົນສຳເລັດ!",
#                 "TID": upload.TID,
#                 "file_id": upload.file_id,
#                 "fileName": upload.fileName,
#                 "fileSize": upload.fileSize,
#                 "path": upload.path,
#                 "insertDate": upload.insertDate.isoformat(),
#                 "summary": {
#                     "total_in_file": len(data),
#                     "duplicates_skipped": len(duplicates),
#                     "new_records_added": len(new_records),
#                     "status": upload.status
#                 }
#             }, status=201)

#         except Exception as e:
#             logger.error(f"Unexpected Error: {str(e)}")
#             return Response({"error": f"ເກີດຄວາມຜິດພາດ: {str(e)}"}, status=500)
        
        
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from rest_framework.response import Response
import math


class UploadFileTelecomPagination(PageNumberPagination):
    page_size = 20  # default limit
    page_size_query_param = 'limit'  # ໃຊ້ 'limit' ແທນ 'page_size'
    page_query_param = 'page'  # ໃຊ້ 'page' ສຳລັບເລກໜ້າ
    max_page_size = 100  # ຈຳກັດສູງສຸດ 100 ລາຍການຕໍ່ໜ້າ

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,  # ເພີ່ມ total_pages
            'current_page': self.page.number,  # ເພີ່ມໜ້າປັດຈຸບັນ
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class UploadFileTelecomListCreate(generics.ListCreateAPIView):
    queryset = UploadFileTelecom.objects.all()
    serializer_class = UploadFileTelecomSerializer
    pagination_class = UploadFileTelecomPagination

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            # ຖ້າສົ່ງມາເປັນ list ສ້າງຫຼາຍ records
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                'success': True,
                'message': f'ສ້າງຂໍ້ມູນສຳເລັດ {len(serializer.data)} ລາຍການ',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            # ຖ້າເປັນ dict ສ້າງ 1 record
            return super().create(request, *args, **kwargs)


class UploadFileTelecomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadFileTelecom.objects.all()
    serializer_class = UploadFileTelecomSerializer


# views.py (ເພີ່ມລົງໄປລຸ່ມ UploadJsonFileView)

class UploadBillJsonFileView(APIView):
    def post(self, request):
        try:
            file_obj = request.FILES.get('file')
            if not file_obj:
                return Response({"error": "ກະລຸນາເລືອກໄຟລ໌"}, status=400)
            if not file_obj.name.lower().endswith('.json'):
                return Response({"error": "ຮອງຮັບແຕ່ .json"}, status=400)

            user_id = request.POST.get('user_id', 'unknown')
            telecom_type = request.POST.get('telecomType', 'Bill')
            period = request.POST.get('period', '')
            stype_id = request.POST.get('stype_id')

            file_id = str(uuid.uuid4())
            size = file_obj.size
            file_size = (
                f"{size} B" if size < 1024 else
                f"{size/1024:.1f} KB" if size < 1024**2 else
                f"{size/(1024**2):.1f} MB" if size < 1024**3 else
                f"{size/(1024**3):.1f} GB"
            )

            # --- ບັນທຶກ log ການອັບໂຫຼດ ---
            upload = UploadFileTelecom(
                fileUpload=file_obj,
                fileName=file_obj.name,
                file_id=file_id,
                user_id=user_id,
                telecomType=telecom_type,
                period=period,
                status='processing',
                status_upload='uploaded',
                FileType='.json',
                fileSize=file_size,
                path='',
                progress_percentage=0,
                percentage=0.0
            )
            if stype_id:
                try:
                    upload.SType = SType.objects.get(id=stype_id)
                except SType.DoesNotExist:
                    pass
            upload.save()
            upload.path = upload.fileUpload.path
            upload.save(update_fields=['path'])

            # --- ອ່ານ JSON ---
            try:
                file_obj.seek(0)
                data = json.load(file_obj)
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError as e:
                upload.status = 'failed'
                upload.save(update_fields=['status'])
                return Response({"error": f"JSON ບໍ່ຖືກຕ້ອງ: {str(e)}"}, status=400)

            # --- ກວດຊ້ຳໂດຍໃຊ້ InvoiceNo ເທົ່ານັ້ນ (ແນະນຳທີ່ສຸດ) ---
            existing_invoices = set(
                Telecom_Bill.objects.filter(
                    InvoiceNo__in=[item.get('InvoiceNo') for item in data if item.get('InvoiceNo')]
                ).values_list('InvoiceNo', flat=True)
            )

            # --- ຟັງຊັນ clean ---
            def clean_value(value):
                if value in [None, 'null', 'NULL', '', '0/0/0 00:00:00']:
                    return None
                return value

            # --- ປະມວນຜົນແຕ່ລະ record ---
            new_bill_records = []
            duplicates = []

            for item in data:
                invoice_no = clean_value(item.get('InvoiceNo'))

                # ຂ້າມຖ້າບໍ່ມີ InvoiceNo
                if not invoice_no:
                    duplicates.append(item)
                    continue

                # ກວດຊ້ຳ
                if invoice_no in existing_invoices:
                    duplicates.append(item)
                    continue

                # ສ້າງ object ແລະເພີ່ມໃສ່ list
                new_bill_records.append(
                    Telecom_Bill(
                        BillID=item.get('BillID'),
                        Customer_ID=clean_value(item.get('Customer_ID')),
                        InvoiceNo=invoice_no,
                        TypeOfPro=clean_value(item.get('TypeOfPro')),
                        Outstanding=item.get('Outstanding') or 0.0,
                        Basic_Tax=item.get('Basic_Tax') or 0.0,
                        Bill_Amount=item.get('Bill_Amount') or 0.0,
                        Debt_Amount=item.get('Debt_Amount') or 0.0,
                        Payment_ID=clean_value(item.get('Payment_ID')),
                        PaymentType=clean_value(item.get('PaymentType')),
                        Payment_Date=clean_value(item.get('Payment_Date')),
                        InvoiceMonth=clean_value(item.get('InvoiceMonth')),
                        InvoiceDate=clean_value(item.get('InvoiceDate')),
                        DisID=clean_value(item.get('DisID')),
                        ProID=clean_value(item.get('ProID')),
                        UserID=user_id,
                    )
                )

            # --- ບັນທຶກລົງ DB ---
            try:
                with transaction.atomic():
                    Telecom_Bill.objects.bulk_create(
                        new_bill_records,
                        ignore_conflicts=True
                    )
                upload.status = 'completed'
                upload.progress_percentage = 100
                upload.percentage = 100.0
                upload.save(update_fields=['status', 'progress_percentage', 'percentage'])

            except Exception as e:
                upload.status = 'failed'
                upload.save(update_fields=['status'])
                logger.error(f"DB Error: {e}")
                return Response({"error": f"ບັນທຶກບໍ່ສຳເລັດ: {str(e)}"}, status=500)

            # --- ສົ່ງຜົນກັບ ---
            return Response({
                "message": "ອັບໂຫຼດແລະປະມວນຜົນໃບບີນສຳເລັດ!",
                "TID": upload.TID,
                "file_id": upload.file_id,
                "fileName": upload.fileName,
                "fileSize": upload.fileSize,
                "path": upload.path,
                "insertDate": upload.insertDate.isoformat(),
                "summary": {
                    "total_in_file": len(data),
                    "duplicates_skipped": len(duplicates),
                    "new_bills_added": len(new_bill_records),
                    "status": upload.status
                }
            }, status=201)

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            return Response({"error": f"ເກີດຄວາມຜິດພາດ: {str(e)}"}, status=500)