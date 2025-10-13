from rest_framework import serializers
from .models import Customer_Info_IND
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from .models import Login, memberInfo, User_Group
from django.core.validators import MaxValueValidator, MinLengthValidator




class CustomerInfoINDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Info_IND
        fields = '__all__'


# serializers.py
from rest_framework import serializers
from .models import SType

class STypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SType
        fields = '__all__'


        
from rest_framework import serializers
from .models import Login

from .models import EnterpriseInfo
class Meta:
         model = EnterpriseInfo
         fields = '__all__'

from .models import bank_bnk
class Bank_InfoINDSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank_bnk
        fields = '_all_' 
        
# get EnterpriseInfo
from rest_framework import serializers
from .models import EnterpriseInfo, InvestorInfo

# class EnterpriseInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EnterpriseInfo
#         fields = '__all__'

class InvestorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInfo
        fields = '__all__'

#  saerch enterprise

# serializers.py
# from rest_framework import serializers
# from .models import EnterpriseInfo

# class EnterpriseInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EnterpriseInfo
#         fields = '__all__'


# lcicHome/serializers.py

from rest_framework import serializers
from .models import EnterpriseInfo




from rest_framework import serializers
from .models import EnterpriseInfo, InvestorInfo


class InvestorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInfo
        fields = '__all__'


# from rest_framework import serializers
# from .models import EnterpriseInfo, InvestorInfo

# class EnterpriseInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EnterpriseInfo
#         fields = '__all__'

class InvestorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInfo
        fields = '__all__'

from .models import H_productInfo
class H_productInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = H_productInfo
        fields = '__all__'
        
        


from .models import B1_Monthly

class B1_MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = B1_Monthly
        fields = '__all__'
        


# from rest_framework import serializers
# from .models import UploadedFile

# class UploadedFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UploadedFile
#         fields = '__all__'



from rest_framework import serializers
from .models import Upload_File

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_File
        fields = '__all__'

from rest_framework import serializers
from .models import  Upload_File_C ,C1, C_error,col_real_estates,col_money_mia, col_equipment_eqi,col_project_prj,col_vechicle_veh,col_guarantor_gua,col_goldsilver_gold,C_error

class col_goldsilver_goldSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_goldsilver_gold
        fields = '__all__'
class C_errorSerializer(serializers.ModelSerializer):
    class Meta:
        model = C_error
        fields = '__all__'
class col_guarantor_guaSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_guarantor_gua
        fields = '__all__'
class col_equipment_eqiSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_equipment_eqi
        fields = '__all__'

class col_vechicle_vehSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_vechicle_veh
        fields = '__all__'
class col_project_prjSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_project_prj
        fields = '__all__'

class col_money_miaSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_money_mia
        fields = '__all__'
class UploadFilecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_File_C
        fields = '__all__'


class C1Serializer(serializers.ModelSerializer):
    class Meta:
        model = C1
        fields = '__all__'
class C_errorSerializer(serializers.ModelSerializer):
    class Meta:
        model = C_error
        fields = '__all__'
class col_real_estatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_real_estates
        fields = '__all__'

from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

from rest_framework import serializers
from .models import B1_Monthly, B_Data_is_damaged, data_edit, B1

class B1MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = B1_Monthly
        fields = '__all__'

class BDataIsDamagedSerializer(serializers.ModelSerializer):
    class Meta:
        model = B_Data_is_damaged
        fields = '__all__'

class DataEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_edit
        fields = '__all__'

class B1Serializer(serializers.ModelSerializer):
    class Meta:
        model = B1
        fields = '__all__'
from rest_framework import serializers
from .models import EnterpriseInfo




# class EnterpriseInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EnterpriseInfo
#         fields = '__all__'

from .models import disputes
class disputesSerializer(serializers.ModelSerializer):
    class Meta:
        model = disputes
        fields = '__all__'


from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
from rest_framework import serializers
from .models import User_Group

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Group
        fields = '__all__'

        
        
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    MID = serializers.PrimaryKeyRelatedField(queryset=memberInfo.objects.all(), allow_null=True, required=False)
    GID = serializers.PrimaryKeyRelatedField(queryset=User_Group.objects.all(), allow_null=True, required=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            raise serializers.ValidationError('Invalid username or password.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid username or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is deactivated.')

        data['user'] = user
        return data

    def to_representation(self, user):
        return {
            'UID': user.UID,
            'MID': {
                'id': user.MID.id,
                'code': user.MID.code
            } if user.MID else None,
            'GID': {
                'GID': user.GID.GID,
                'nameL': user.GID.nameL
            } if user.GID else None,
            'username': user.username,
            'nameL': user.nameL,
            'nameE': user.nameE,
            'surnameL': user.surnameL,
            'surnameE': user.surnameE,
            'is_active': user.is_active,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
        }
class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberInfo
        fields = ['code', 'nameL','nameE']  

from rest_framework import serializers
from .models import User_Group

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Group
        fields = ['GID', 'nameL', 'nameE']


# serializers.py
# serializers.py
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .models import Login, User_Group, memberInfo

class LoginSerializer(serializers.ModelSerializer):
    """
    Clean and secure serializer for Login (User) model with bank code validation
    """
    profile_image = serializers.ImageField(required=False, allow_null=True)
    profile_image_url = serializers.SerializerMethodField(read_only=True)
    MID = serializers.PrimaryKeyRelatedField(
        queryset=memberInfo.objects.all(),
        required=False,
        allow_null=True
    )
    GID = serializers.PrimaryKeyRelatedField(
        queryset=User_Group.objects.all(),
        required=False,
        allow_null=True
    )
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Login
        fields = [
            'UID', 'username', 'password', 'confirm_password',
            'nameL', 'surnameL', 'nameE', 'surnameE',
            'MID', 'GID', 'branch_id', 'bnk_code',
            'profile_image', 'profile_image_url', 'is_active'
        ]
        extra_kwargs = {
            'username': {'required': True},
            'nameL': {'required': True},
            'surnameL': {'required': True},
        }

    def get_profile_image_url(self, obj):
        """Return profile image URL if exists"""
        return f'/{obj.profile_image.name}' if obj.profile_image else None

    def validate(self, attrs):
        """Custom validation for password matching and bank code consistency"""
        # Password validation
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({
                'password': 'Passwords do not match.'
            })
        
        # Profile image validation
        profile_image = attrs.get('profile_image')
        if profile_image:
            # Check file size (5MB limit)
            if profile_image.size > 5 * 1024 * 1024:
                raise serializers.ValidationError({
                    'profile_image': 'File size must be less than 5MB.'
                })
            
            # Check file type
            allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']
            if hasattr(profile_image, 'content_type') and profile_image.content_type not in allowed_types:
                raise serializers.ValidationError({
                    'profile_image': 'Only JPEG, PNG and GIF files are allowed.'
                })
        
        # Bank code validation - ensure consistency with memberInfo
        bnk_code = attrs.get('bnk_code')
        mid = attrs.get('MID')
        
        if bnk_code and mid:
            if mid.bnk_code != bnk_code:
                raise serializers.ValidationError({
                    'bnk_code': f'Bank code mismatch. Expected: {mid.bnk_code}, Got: {bnk_code}'
                })
        
        # If MID is provided but no bnk_code, auto-assign from memberInfo
        if mid and not bnk_code:
            attrs['bnk_code'] = mid.bnk_code
            
        return attrs

    def validate_username(self, value):
        """Ensure username is unique and follows rules"""
        if Login.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists.')
        return value.strip().lower()

    def create(self, validated_data):
        """Create user with proper password hashing and bank code handling"""
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password')
        
        # Create user instance
        user = Login.objects.create(**validated_data)
        user.set_password(password)  # Properly hash password
        user.save()
        
        return user

    def update(self, instance, validated_data):
        """Update user with proper validation"""
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)
        
        # Handle password update
        if password:
            instance.set_password(password)
        
        # Handle bank code consistency on update
        bnk_code = validated_data.get('bnk_code')
        mid = validated_data.get('MID')
        
        if mid and bnk_code and mid.bnk_code != bnk_code:
            raise serializers.ValidationError({
                'bnk_code': 'Bank code must match the selected member info.'
            })
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

from rest_framework import serializers
from .models import memberInfo


        
        

from .models import SidebarItem, SidebarSubItem, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        # fields = ['id', 'name','name_la', 'can_access_all_paths']
        fields = '__all__'


# class SidebarItemSerializer(serializers.ModelSerializer):
#     roles = RoleSerializer(many=True, read_only=True)

#     class Meta:
#         model = SidebarItem
#         fields = ['id', 'name', 'url', 'roles']

# class SidebarSubItemSerializer(serializers.ModelSerializer):
#     parent = SidebarItemSerializer(read_only=True)
#     roles = RoleSerializer(many=True, read_only=True)

#     class Meta:
#         model = SidebarSubItem
#         fields = ['id', 'name', 'url', 'parent', 'roles']


class SidebarSubItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidebarSubItem
        fields = ['id', 'name', 'url', 'parent', 'roles']
    
    def validate(self, data):
        # Ensure parent exists when creating sub-item
        if 'parent' in data and not SidebarItem.objects.filter(id=data['parent'].id).exists():
            raise serializers.ValidationError("Invalid parent item")
        return data
class SidebarItemSerializer(serializers.ModelSerializer):
    sub_items = SidebarSubItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = SidebarItem
        fields = ['id', 'name', 'url', 'icon', 'roles', 'sub_items']
    
    def to_representation(self, instance):
        """Include sub_items in the response"""
        representation = super().to_representation(instance)
        representation['sub_items'] = SidebarSubItemSerializer(
            instance.sub_items.all(), 
            many=True
        ).data
        return representation

from .models import Customer_Info_IND,EnterpriseInfo, InvestorInfo, bank_bnk, B1_Yearly, B1
from django.core.validators import MinLengthValidator

class CustomerInfoINDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Info_IND
        fields = '_all_'
        
class Bank_InfoINDSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank_bnk 
        fields = '__all__'
        
# serializers.py
from rest_framework import serializers
from .models import EnterpriseInfo

class EnterpriseInfoSerializer(serializers.ModelSerializer):
    # ເພີ່ມ field ນີ້ເພື່ອຮັບ collateral_id (ແຕ່ບໍ່ບັນທຶກລົງ database)
    collateral_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = EnterpriseInfo
        fields = '__all__'
        read_only_fields = ['LCICID', 'InsertDate', 'LCIC_code']  # LCIC_code ຈະຖືກສ້າງອັດຕະໂນມັດ
    
    def create(self, validated_data):
        # ລຶບ collateral_id ອອກກ່ອນສ້າງ Enterprise
        validated_data.pop('collateral_id', None)
        return super().create(validated_data)
        
class B1_YearlySerializer(serializers.ModelSerializer):
    class Meta:
        model = B1_Yearly
        fields = '_all_'

from .models import searchLog

class SearchLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = searchLog
        fields = '__all__' 

from .models import request_charge
class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = request_charge
        fields = '__all__' 

from .models import Main_catalog_cat
class MainCatalogCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_catalog_cat
        fields = '__all__'

from .models import request_charge
class RequestChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = request_charge
        fields = '__all__'
        

from .models import memberInfo
class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberInfo
        fields = '__all__'
        
from .models import Province, District, Village

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['Prov_ID', 'Province_Name']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['ID', 'Prov_ID', 'Dstr_ID', 'District_Name']

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ['ID', 'Prov_ID', 'Dstr_ID', 'Vill_ID', 'Village_Name']

from .models import ReportCatalog
# class ReportCatalogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ReportCatalog
#         fields = '__all__'

class ReportCatalogSerializer(serializers.ModelSerializer):
    Report_UserRole = serializers.PrimaryKeyRelatedField(queryset=User_Group.objects.all(), many=True)

    class Meta:
        model = ReportCatalog
        fields = ['Report_Name', 'Report_UserRole']  # Explicitly list the fields you want

    def create(self, validated_data):
        # Extract the user roles from the validated data
        user_roles = validated_data.pop('Report_UserRole')
        # Create the report catalog entry
        report_catalog = ReportCatalog.objects.create(**validated_data)
        # Add the many-to-many relationship (user roles)
        report_catalog.Report_UserRole.set(user_roles)
        return report_catalog

    def update(self, instance, validated_data):
        # Handle updating existing report catalog
        user_roles = validated_data.pop('Report_UserRole')
        instance.Report_Name = validated_data.get('Report_Name', instance.Report_Name)
        instance.save()
        instance.Report_UserRole.set(user_roles)  # Update the many-to-many relationship
        return instance
from rest_framework import serializers
from .models import Search_batfile

class SearchBatfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search_batfile
        fields = '__all__'
from rest_framework import serializers
from .models import bank_branch
from .models import DataSubmitUtility


class BankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank_branch
        fields = '__all__'  # Include all fields from the model
class DataSubmitUtilitySerializer (serializers.ModelSerializer):
    class Meta:
        model = DataSubmitUtility
        fields = '__all__'
        
from utility.models import FileDetail

class FileDetailSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    insertDate = serializers.SerializerMethodField()

    class Meta:
        model = FileDetail
        fields = ['id', 'file_name', 'insertDate', 'status']  # Status is now a direct field

    def get_file_name(self, obj):
        return obj.name
    
    def get_insertDate(self, obj):
        return obj.created_at

from utility.models import File_Electric
class FileElectricSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    insertDate = serializers.SerializerMethodField()

    class Meta:
        model = File_Electric
        fields = ['id', 'file_name', 'insertDate', 'status']

    def get_file_name(self, obj):
        return obj.name
    
    def get_insertDate(self, obj):
        return obj.created_at

from rest_framework import serializers
from utility.models import w_customer_info, Utility_Bill
class WaterCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = w_customer_info
        fields = ['Customer_ID', 'Company_name', 'Name', 'Surname', 'National_ID', 
                 'Passport', 'Address', 'Dustrict_ID', 'Province_ID', 'Tel', 
                 'Email', 'Cus_type', 'Regis_date']

from utility.models import Utility_Bill
class UtilityBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility_Bill
        fields = ['BillID', 'Customer_ID', 'InvoiceNo', 'TypeOfPro', 'Outstanding',
                 'Basic_Tax', 'Bill_Amount', 'Debt_Amount', 'Payment_ID',
                 'PaymentType', 'Payment_Date', 'InvoiceMonth', 'InvoiceDate',
                 'DisID', 'ProID', 'InsertDate', 'UpdateDate', 'UserID']

from utility.models import edl_customer_info
class EDLCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = edl_customer_info
        fields = ['Customer_ID', 'Company_name', 'Name', 'Surname', 'National_ID', 
                 'Passport', 'Address', 'Dustrict_ID', 'Province_ID', 'Tel', 
                 'Email', 'Cus_type', 'Regis_date']
from utility.models import Electric_Bill       
class ElectricBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electric_Bill
        fields = ['BillID', 'Customer_ID', 'InvoiceNo', 'TypeOfPro', 'Outstanding',
                 'Basic_Tax', 'Bill_Amount', 'Debt_Amount', 'Payment_ID',
                 'PaymentType', 'Payment_Date', 'InvoiceMonth', 'InvoiceDate',
                 'DisID', 'ProID', 'InsertDate', 'UpdateDate', 'UserID']

from utility.models import searchlog_utility
class SearchLogUtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = searchlog_utility
        fields = ['search_id', 'bnk_code', 'sys_usr', 'wt_cusid', 'edl_cusid', 'tel_cusid',
                  'proID_edl', 'proID_wt', 'proID_tel', 'credittype', 'inquiry_date', 'inquiry_time']

from utility.models import edl_province_code, edl_district_code
class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = edl_province_code
        fields = ['pro_id', 'pro_name']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = edl_district_code
        fields = ['dis_id', 'dis_name']

class ProvinceWithDistrictsSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)
    
    class Meta:
        model = edl_province_code
        fields = ['pro_id', 'pro_name', 'districts']
    
class ProvinceDistrictSerializer(serializers.Serializer):
    pro_id = serializers.CharField()
    pro_name = serializers.CharField()
    dis_id = serializers.CharField()
    dis_name = serializers.CharField()

from rest_framework import serializers
from .models import LCICSystemUser
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from .models import LCICSystemUser
from django.contrib.auth.hashers import make_password
class LCICSystemUserSerializer(serializers.ModelSerializer):
    # Use SerializerMethodField for reading (output)
    profile_image_url = serializers.SerializerMethodField()
    # Use ImageField for writing (input)
    profile_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = LCICSystemUser
        fields = [
            'id',
            'bnk_code',
            'branch_code',
            'username',
            'password',
            'roles',
            'nameL',
            'nameE',
            'surnameL',
            'surnameE',
            'profile_image',  # Include for writing
            'profile_image_url',  # Include for reading
            'is_active',
            'insertDate'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'profile_image': {'required': False},
        }

    def get_profile_image_url(self, obj):
        if obj.profile_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile_image.url)
            return obj.profile_image.url
        return None

    def validate_profile_image(self, value):
        if value:
            if value.size > 5 * 1024 * 1024:  # 5MB limit
                raise serializers.ValidationError('Image size should be less than 5 MB')
            if not value.content_type.startswith('image/'):
                raise serializers.ValidationError('File must be an image')
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return LCICSystemUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('Updating instance with validated data:', validated_data)  # Debug
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        # Explicitly handle profile_image
        if 'profile_image' in validated_data:
            if instance.profile_image:
                instance.profile_image.delete(save=False)  # Delete old image
            instance.profile_image = validated_data['profile_image']
        return super().update(instance, validated_data)


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LCICSystemUser
        fields = ['username', 'bnk_code', 'branch_code', 'roles',
                 'nameL', 'nameE', 'surnameL', 'surnameE', 'last_login']
from .models import ChargeMatrix
class ChargeMatrixSerializer (serializers.ModelSerializer):
    class Meta:
        model = ChargeMatrix
        fields = '__all__'
        
from .models import bank_bnk

class BankSerializer(serializers.ModelSerializer):
    # Read-only field for image URL
    bnk_images_url = serializers.SerializerMethodField()
    # Writeable field for image upload
    bnk_images = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = bank_bnk
        fields = [
            'bnk_sys_id',
            'bnk_code',
            'bnk_short_form',
            'bnk_images',
            'bnk_images_url',
            'bnk_name',
            'bnk_lao_name',
            'bnk_insert_date',
            'bnk_type',
        ]
        extra_kwargs = {
            'bnk_sys_id': {'read_only': True},
            'bnk_insert_date': {'required': False},
        }

    def get_bnk_images_url(self, obj):
        if obj.bnk_images:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.bnk_images.url)
            return obj.bnk_images.url
        return None

    def validate_bnk_images(self, value):
        if value:
            if value.size > 5 * 1024 * 1024:  # 5MB limit
                raise serializers.ValidationError('Image size should be less than 5 MB')
            if not value.content_type.startswith('image/'):
                raise serializers.ValidationError('File must be an image')
        return value

    def create(self, validated_data):
        return bank_bnk.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('Updating instance with validated data:', validated_data)  # Debug
        # Handle bnk_images update
        if 'bnk_images' in validated_data:
            if instance.bnk_images:
                instance.bnk_images.delete(save=False)  # Delete old image
            instance.bnk_images = validated_data['bnk_images']
        return super().update(instance, validated_data)
    
    
# # API Tracking EDL ----------------------------------
from rest_framework import serializers
from utility.models import UploadDataTracking, UploadLog

class UploadLogSerializer(serializers.ModelSerializer):
    """Serializer for upload logs"""
    
    class Meta:
        model = UploadLog
        fields = ['id', 'log_level', 'message', 'timestamp']
        read_only_fields = ['id', 'timestamp']

class UploadTrackingSerializer(serializers.ModelSerializer):
    upload_duration = serializers.SerializerMethodField()
    status_color = serializers.SerializerMethodField()
    formatted_size = serializers.SerializerMethodField()
    success_rate_formatted = serializers.SerializerMethodField()
    
    class Meta:
        model = UploadDataTracking
        fields = [
            'id', 'pro_id', 'pro_name', 'dis_id', 'dis_name', 
            'upload_month', 'status', 'status_color', 'total_records', 
            'processed_records', 'failed_records', 'success_rate_formatted',
            'data_size_mb', 'formatted_size', 'upload_started','payment_records',   # ✅ ADD THIS
            'customer_records',  # ✅ ADD THIS 
            'upload_completed', 'upload_duration', 'user_upload', 
            'created_at', 'updated_at'
        ]
    
    def get_upload_duration(self, obj):
        duration = obj.upload_duration
        if duration:
            if duration < 60:
                return f"{duration:.1f}s"
            elif duration < 3600:
                return f"{duration/60:.1f}m"
            else:
                return f"{duration/3600:.1f}h"
        return None
    
    def get_status_color(self, obj):
        colors = {
            'pending': 'orange',
            'in_progress': 'blue',
            'completed': 'green',
            'failed': 'red',
            'partial': 'amber'
        }
        return colors.get(obj.status, 'grey')
    
    def get_formatted_size(self, obj):
        if obj.data_size_mb < 1:
            return f"{obj.data_size_mb * 1024:.1f} KB"
        elif obj.data_size_mb < 1024:
            return f"{obj.data_size_mb:.1f} MB"
        else:
            return f"{obj.data_size_mb / 1024:.1f} GB"
    
    def get_success_rate_formatted(self, obj):
        return f"{obj.success_rates:.1f}%"


class UploadTrackingDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for upload tracking with logs"""
    logs = UploadLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = UploadDataTracking
        fields = [
            'id', 'pro_id', 'pro_name', 'dis_id', 'dis_name', 
            'upload_month', 'status', 'total_records', 'processed_records', 
            'failed_records', 'data_size_mb', 'upload_started', 
            'upload_completed', 'user_upload', 'success_rates',
            'error_message', 'api_response_code', 'logs',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class ProvinceDistrictSerializer(serializers.Serializer):
    """Serializer for province/district data from external API"""
    pro_id = serializers.CharField(max_length=10)
    pro_name = serializers.CharField(max_length=100)
    dis_id = serializers.CharField(max_length=10)
    dis_name = serializers.CharField(max_length=100)



    
    
# minimal_serializers.py - Use this for initial setup

from rest_framework import serializers
from utility.models import UploadDataTracking, UploadLog

class MinimalUploadTrackingSerializer(serializers.ModelSerializer):
    """Minimal serializer that handles missing fields gracefully"""
    
    upload_duration = serializers.SerializerMethodField()
    status_color = serializers.SerializerMethodField()
    formatted_size = serializers.SerializerMethodField()
    success_rate_formatted = serializers.SerializerMethodField()
    
    # Handle potentially missing fields
    processed_records = serializers.SerializerMethodField()
    failed_records = serializers.SerializerMethodField()
    
    class Meta:
        model = UploadDataTracking
        fields = [
            'id', 'pro_id', 'pro_name', 'dis_id', 'dis_name', 
            'upload_month', 'status', 'status_color', 'total_records', 
            'processed_records', 'failed_records', 'success_rate_formatted',
            'data_size_mb', 'formatted_size', 'upload_started', 
            'upload_completed', 'upload_duration', 'user_upload', 
            'created_at', 'updated_at'
        ]
    
    def get_processed_records(self, obj):
        """Handle missing processed_records field"""
        try:
            return getattr(obj, 'processed_records', 0)
        except AttributeError:
            return 0
    
    def get_failed_records(self, obj):
        """Handle missing failed_records field"""
        try:
            return getattr(obj, 'failed_records', 0)
        except AttributeError:
            return 0
    
    def get_upload_duration(self, obj):
        try:
            duration = obj.upload_duration
            if duration:
                if duration < 60:
                    return f"{duration:.1f}s"
                elif duration < 3600:
                    return f"{duration/60:.1f}m"
                else:
                    return f"{duration/3600:.1f}h"
            return None
        except Exception:
            return None
    
    def get_status_color(self, obj):
        colors = {
            'pending': 'orange',
            'in_progress': 'blue',
            'completed': 'green',
            'failed': 'red',
            'partial': 'amber'
        }
        return colors.get(obj.status, 'grey')
    
    def get_formatted_size(self, obj):
        try:
            size_mb = getattr(obj, 'data_size_mb', 0) or 0
            if size_mb < 1:
                return f"{size_mb * 1024:.1f} KB"
            elif size_mb < 1024:
                return f"{size_mb:.1f} MB"
            else:
                return f"{size_mb / 1024:.1f} GB"
        except Exception:
            return "0 KB"
    
    def get_success_rate_formatted(self, obj):
        try:
            processed = self.get_processed_records(obj)
            total = getattr(obj, 'total_records', 0) or 0
            if total > 0:
                rate = (processed / total) * 100
                return f"{rate:.1f}%"
            return "0.0%"
        except Exception:
            return "0.0%"

class MinimalUploadLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadLog
        fields = ['id', 'log_level', 'message', 'timestamp']

class MinimalUploadTrackingDetailSerializer(MinimalUploadTrackingSerializer):
    logs = MinimalUploadLogSerializer(many=True, read_only=True)
    
    class Meta(MinimalUploadTrackingSerializer.Meta):
        fields = MinimalUploadTrackingSerializer.Meta.fields + [
            'error_message', 'api_response_code', 'logs'
        ]



# Water Supply Data Load Tracking --------------------------------------------------

from utility.models import WaterUploadDataTracking, WaterUploadLog

class WaterUploadTrackingSerializer(serializers.ModelSerializer):
    """Serializer for water supply upload tracking list view"""
    
    formatted_month = serializers.ReadOnlyField()
    success_rate_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = WaterUploadDataTracking
        fields = [
            'id',
            'upload_month',
            'formatted_month',
            'status',
            'description',
            'total_records',
            'processed_records',
            'failed_records',
            'success_rates',
            'success_rate_percentage',
            'data_size_mb',
            'api_response_code',
            'upload_started',
            'upload_completed', 
            'upload_duration',
            'user_upload',
            'error_message',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id', 
            'created_at', 
            'updated_at',
            'formatted_month',
            'success_rate_percentage'
        ]

class WaterUploadLogSerializer(serializers.ModelSerializer):
    """Serializer for water supply upload logs"""
    
    formatted_timestamp = serializers.ReadOnlyField()
    
    class Meta:
        model = WaterUploadLog
        fields = [
            'id',
            'timestamp',
            'formatted_timestamp',
            'log_level',
            'message',
            'context_data'
        ]
        read_only_fields = ['id', 'timestamp', 'formatted_timestamp']

class WaterUploadTrackingDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for water supply upload tracking with logs"""
    
    logs = WaterUploadLogSerializer(many=True, read_only=True)
    formatted_month = serializers.ReadOnlyField()
    success_rate_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = WaterUploadDataTracking
        fields = [
            'id',
            'upload_month',
            'formatted_month',
            'status',
            'description',
            'total_records',
            'processed_records',
            'failed_records',
            'success_rates',
            'success_rate_percentage',
            'data_size_mb',
            'api_response_code',
            'upload_started',
            'upload_completed',
            'upload_duration',
            'user_upload',
            'error_message',
            'created_at',
            'updated_at',
            'logs'
        ]
        read_only_fields = [
            'id', 
            'created_at', 
            'updated_at',
            'formatted_month',
            'success_rate_percentage',
            'logs'
        ]

class WaterSupplyUploadRequestSerializer(serializers.Serializer):
    """Serializer for water supply upload request"""
    
    month = serializers.CharField(
        max_length=6,
        help_text="Month in MMYYYY format (e.g., 122024)"
    )
    username = serializers.CharField(
        max_length=100,
        default='system'
    )
    api_token = serializers.CharField(
        max_length=500,
        help_text="Bearer token for water supply API authentication",
        style={'input_type': 'password'}  # Hide token in browsable API
    )
    
    def validate_month(self, value):
        """Validate month format"""
        if not value or len(value) != 6:
            raise serializers.ValidationError("Month must be in MMYYYY format (e.g., 122024)")
        
        try:
            month_part = value[:2]
            year_part = value[2:]
            
            # Validate month (01-12)
            month_int = int(month_part)
            if month_int < 1 or month_int > 12:
                raise serializers.ValidationError("Month part must be between 01 and 12")
            
            # Validate year (reasonable range)
            year_int = int(year_part)
            if year_int < 2020 or year_int > 2030:
                raise serializers.ValidationError("Year part must be between 2020 and 2030")
                
        except ValueError:
            raise serializers.ValidationError("Month must contain only numeric characters")
        
        return value
    
    def validate_api_token(self, value):
        """Basic validation for API token"""
        if not value or len(value.strip()) < 10:
            raise serializers.ValidationError("API token is required and must be at least 10 characters")
        return value.strip()

class WaterTrackingInitializationSerializer(serializers.Serializer):
    """Serializer for initializing water supply tracking"""
    
    month = serializers.CharField(
        max_length=6,
        help_text="Month in MMYYYY format (e.g., 122024)"
    )
    username = serializers.CharField(
        max_length=100,
        default='system'
    )
    
    def validate_month(self, value):
        """Validate month format"""
        if not value or len(value) != 6:
            raise serializers.ValidationError("Month must be in MMYYYY format (e.g., 122024)")
        
        try:
            month_part = value[:2]
            year_part = value[2:]
            
            month_int = int(month_part)
            if month_int < 1 or month_int > 12:
                raise serializers.ValidationError("Month part must be between 01 and 12")
            
            year_int = int(year_part)
            if year_int < 2020 or year_int > 2030:
                raise serializers.ValidationError("Year part must be between 2020 and 2030")
                
        except ValueError:
            raise serializers.ValidationError("Month must contain only numeric characters")
        
        return value

# Statistics serializers for dashboard
class WaterSupplyStatisticsSerializer(serializers.Serializer):
    """Serializer for water supply statistics"""
    
    total_uploads = serializers.IntegerField()
    status_breakdown = serializers.DictField()
    total_data_size_mb = serializers.FloatField()
    total_records = serializers.IntegerField()
    
    # Additional computed fields
    avg_success_rate = serializers.FloatField(required=False)
    avg_upload_duration = serializers.FloatField(required=False)
    last_upload_date = serializers.DateTimeField(required=False)

class WaterSupplyDashboardSerializer(serializers.Serializer):
    """Serializer for water supply dashboard response"""
    
    data = WaterUploadTrackingSerializer(many=True)
    statistics = WaterSupplyStatisticsSerializer()
    month = serializers.CharField()
    total_count = serializers.IntegerField()