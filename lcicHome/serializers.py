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
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from .models import Login, memberInfo, User_Group

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


class SidebarItemSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = SidebarItem
        fields = ['id', 'name', 'url', 'roles']

class SidebarSubItemSerializer(serializers.ModelSerializer):
    parent = SidebarItemSerializer(read_only=True)
    roles = RoleSerializer(many=True, read_only=True)

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