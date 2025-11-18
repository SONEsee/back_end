#serializers.py
from rest_framework import serializers
from utility.models import JsonfileWater,UploadJsonFiles,SType, TelecomCustomer, UploadFileTelecom, Telecom_Bill

class JsonfileWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonfileWater
        fields = '__all__'
        
class UploadJsonFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadJsonFiles 
        fields = '__all__'

class STypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SType
        fields = '__all__'
    def validate_SType(self, value):
        if not value:
            raise serializers.ValidationError("SType ບໍ່ສາມາດເປັນຄ່າວ່າງໄດ້")
        return value  

class TelecomCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelecomCustomer
        fields = '__all__'

class UploadFileTelecomSerializer(serializers.ModelSerializer):
    fileUpload = serializers.FileField(read_only=True)  # ຖ້າບໍ່ຕ້ອງການແກ້ໄຟລ໌
    path = serializers.CharField(read_only=True)
    insertDate = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = UploadFileTelecom
        fields = [
            'TID', 'file_id', 'fileName', 'fileSize', 'path', 'user_id',
            'telecomType', 'period', 'status', 'status_upload', 'FileType',
            'progress_percentage', 'percentage', 'insertDate', 'fileUpload'
        ]
        read_only_fields = ['TID', 'file_id', 'path', 'insertDate', 'fileUpload']

# serializers.py
class TelecomBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telecom_Bill
        fields = '__all__'
        extra_kwargs = {
            'Payment_ID': {'allow_null': True, 'required': False},
            'PaymentType': {'allow_null': True, 'required': False},
            'Payment_Date': {'allow_null': True, 'required': False},
            'InvoiceDate': {'allow_null': True, 'required': False},
            'DisID': {'allow_null': True, 'required': False},
        }

    def to_internal_value(self, data):
        # ແປງ "null" string → None
        for field in ['Payment_ID', 'PaymentType', 'DisID', 'Payment_Date', 'InvoiceDate']:
            if data.get(field) in ['null', 'NULL', '', '0/0/0 00:00:00']:
                data[field] = None
        return super().to_internal_value(data)