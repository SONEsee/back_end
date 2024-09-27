from rest_framework import serializers
from .models import Customer_Info_IND,EnterpriseInfo, InvestorInfo, bank_bnk, B1_Yearly, B1
from django.core.validators import MinLengthValidator

class CustomerInfoINDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Info_IND
        fields = '__all__'
        
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
        fields = '__all__'

class B1Serializer(serializers.ModelSerializer):
    class Meta:
        model = B1
        fields = '__all__'
        
class InvestorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInfo
        fields = '__all__'
        
from rest_framework import serializers
from .models import InvestorInfo
class InvestorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInfo
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


from .models import User_Login, Login, memberInfo
from rest_framework import serializers

# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = User_Login
#         fields = '__all__'

from rest_framework import serializers
from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    MID = serializers.PrimaryKeyRelatedField(queryset=memberInfo.objects.all(), allow_null=True, required=False)
    GID = serializers.PrimaryKeyRelatedField(queryset=User_Group.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Login
        fields = ['UID', 'MID', 'GID', 'username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'is_active', 'is_staff', 'is_superuser']

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
        """
        This method is used to control how the data is represented in the response.
        """
        # user = instance['user']  # Get the validated user object

        return {
            'UID': user.UID,
            # 'MID': user.MID.id if user.MID else None,
            # 'GID': user.GID.GID if user.GID else None,
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
        fields = ['code', 'nameL','nameE']  # Adjust fields as needed
        
        

from .models import SidebarItem, SidebarSubItem, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

# class SidebarSubItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SidebarSubItem
#         fields = ['name', 'url']

# class SidebarItemSerializer(serializers.ModelSerializer):
#     sub_items = SidebarSubItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = SidebarItem
#         fields = ['name', 'url', 'sub_items']
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

