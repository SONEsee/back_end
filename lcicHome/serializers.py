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
from .models import User_Group

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Group
        fields = '__all__'


from .models import User_Login
from rest_framework import serializers

# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = User_Login
#         fields = '__all__'

# paylay Backend
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)

#     class Meta:
#         model = Login
#         fields = ['UID', 'MID', 'GID', 'username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'is_active', 'is_staff', 'is_superuser']

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         try:
#             user = Login.objects.get(username=username)
#         except Login.DoesNotExist:
#             raise serializers.ValidationError('Invalid username or password.')

#         if not user.check_password(password):
#             raise serializers.ValidationError('Invalid username or password.')

#         if not user.is_active:
#             raise serializers.ValidationError('User is deactivated.')

#         data['user'] = user
#         return data
    
#     def to_representation(self, user):
#         """
#         This method is used to control how the data is represented in the response.
#         """
#         # user = instance['user']  # Get the validated user object

#         return {
#             'UID': user.UID,
#             'MID': user.MID.id,
#             'GID': user.GID.GID,
#             'username': user.username,
#             'nameL': user.nameL,
#             'nameE': user.nameE,
#             'surnameL': user.surnameL,
#             'surnameE': user.surnameE,
#             'is_active': user.is_active,
#             'is_staff': user.is_staff,
#             'is_superuser': user.is_superuser,
#         }

        
from rest_framework import serializers
from .models import Login

#paylay Backend
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Login
#         fields = ['UID', 'username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'is_active']
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[MinLengthValidator(8)])
    MID = serializers.PrimaryKeyRelatedField(queryset=memberInfo.objects.all(), allow_null=True, required=False)
    GID = serializers.PrimaryKeyRelatedField(queryset=User_Group.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Login
        fields = ['UID', 'MID', 'GID', 'username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'insertDate', 'updateDate', 'is_active', 'is_staff', 'is_superuser', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Ensure the password is hashed
        user = Login.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Hashing should happen inside create_user
            MID=validated_data.get('MID', None),
            GID=validated_data.get('GID', None),
            nameL=validated_data['nameL'],
            nameE=validated_data['nameE'],
            surnameL=validated_data['surnameL'],
            surnameE=validated_data['surnameE'],
            is_active=validated_data.get('is_active', True),
            is_staff=validated_data.get('is_staff', False),
            is_superuser=validated_data.get('is_superuser', False),
        )
        print("AddUser: ", user)
        return user



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

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Unable to log in with provided credentials.")
# from rest_framework import serializers
# from .models import Login

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Login
#         fields = ['username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'GID', 'MID', 'is_active']


# Paylay Pherm 
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)
#     MID = serializers.PrimaryKeyRelatedField(queryset=memberInfo.objects.all(), allow_null=True, required=False)
#     GID = serializers.PrimaryKeyRelatedField(queryset=User_Group.objects.all(), allow_null=True, required=False)

#     class Meta:
#         model = Login
#         fields = ['UID', 'MID', 'GID', 'username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'is_active', 'is_staff', 'is_superuser']

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         try:
#             user = Login.objects.get(username=username)
#         except Login.DoesNotExist:
#             raise serializers.ValidationError('Invalid username or password.')

#         if not user.check_password(password):
#             raise serializers.ValidationError('Invalid username or password.')

#         if not user.is_active:
#             raise serializers.ValidationError('User is deactivated.')

#         data['user'] = user
#         return data
    
#     def to_representation(self, user):
#         """
#         This method is used to control how the data is represented in the response.
#         """
#         # user = instance['user']  # Get the validated user object

#         return {
#             'UID': user.UID,

#             'MID': {
#                 'id': user.MID.id,
#                 'code': user.MID.code
#             } if user.MID else None,
#             'GID': {
#                 'GID': user.GID.GID,
#                 'nameL': user.GID.nameL
#             } if user.GID else None,
#             'username': user.username,
#             'nameL': user.nameL,
#             'nameE': user.nameE,
#             'surnameL': user.surnameL,
#             'surnameE': user.surnameE,
#             'is_active': user.is_active,
#             'is_staff': user.is_staff,
#             'is_superuser': user.is_superuser,
#         }
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

from rest_framework import serializers
from .models import Login, User_Group, memberInfo
from django.core.validators import MinLengthValidator

class LoginSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)  # Ensure profile_image is optional
    password = serializers.CharField(write_only=True, validators=[MinLengthValidator(8)])
    MID = serializers.PrimaryKeyRelatedField(queryset=memberInfo.objects.all(), allow_null=True, required=False)
    GID = serializers.PrimaryKeyRelatedField(queryset=User_Group.objects.all(), allow_null=True, required=False)
    
    
    class Meta:
        model = Login
        fields = ['UID', 'MID', 'GID', 'username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'profile_image', 'insertDate', 'updateDate', 'is_active', 'is_staff', 'is_superuser', 'password','bnk_code','branch_id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract the profile image from validated_data
        profile_image = validated_data.pop('profile_image', None)
        
        # Ensure the password is hashed
        user = Login.objects.create_user(
            bnk_code=validated_data.get('bnk_code', None),
            branch_id=validated_data.get('branch_id', None),
            username=validated_data['username'],
            password=validated_data['password'],
            MID=validated_data.get('MID', None),
            GID=validated_data.get('GID', None),
            nameL=validated_data['nameL'],
            nameE=validated_data['nameE'],
            surnameL=validated_data['surnameL'],
            surnameE=validated_data['surnameE'],
            is_active=validated_data.get('is_active', True),
            is_staff=validated_data.get('is_staff', False),
            is_superuser=validated_data.get('is_superuser', False),
        )
        
        # If a profile image was provided, save it to the user instance
        if profile_image:
            user.profile_image = profile_image
            user.save()

        return user
    
    def update(self, instance, validated_data):
        # Handle password hashing if password is being updated
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # Hash the password using set_password()

        # Update the other fields normally
        instance.username = validated_data.get('username', instance.username)
        instance.nameL = validated_data.get('nameL', instance.nameL)
        instance.nameE = validated_data.get('nameE', instance.nameE)
        instance.surnameL = validated_data.get('surnameL', instance.surnameL)
        instance.surnameE = validated_data.get('surnameE', instance.surnameE)
        instance.MID = validated_data.get('MID', instance.MID)
        instance.GID = validated_data.get('GID', instance.GID)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        bnk_code = validated_data.get('bnk_code', instance.bnk_code)
        branch_id = validated_data.get('branch_id', instance.branch_id)

        # Save the updated user object
        instance.save()
        return instance

from rest_framework import serializers
from .models import memberInfo

class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberInfo
        fields = ['code', 'nameL','nameE']  
        
        

from .models import SidebarItem, SidebarSubItem, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


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


class SidebarItemSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    class Meta:
        model = SidebarItem
        fields = ['id', 'name', 'url','icon', 'roles']


class SidebarSubItemSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    class Meta:
        model = SidebarSubItem
        fields = ['id', 'name', 'url', 'parent', 'roles']

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
        
class EnterpriseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseInfo
        fields = '__all__'
        
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
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

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