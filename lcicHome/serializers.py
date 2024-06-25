from rest_framework import serializers
from .models import Customer_Info_IND

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

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User_Login
        fields = '__all__'
        
from rest_framework import serializers
from .models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['UID', 'username', 'nameL', 'nameE', 'surnameL', 'surnameE', 'is_active']


from .models import EnterpriseInfo
class Meta:
         model = EnterpriseInfo
         fields = '__all__'
         
        
        
# get EnterpriseInfo
from rest_framework import serializers
from .models import EnterpriseInfo, InvestorInfo

class EnterpriseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseInfo
        fields = '__all__'

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

class EnterpriseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseInfo
        fields = '__all__'


from rest_framework import serializers
from .models import EnterpriseInfo, InvestorInfo

class EnterpriseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseInfo
        fields = '__all__'

class InvestorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorInfo
        fields = '__all__'


from rest_framework import serializers
from .models import EnterpriseInfo, InvestorInfo

class EnterpriseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseInfo
        fields = '__all__'

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
        
        
# serializers.py
from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['name', 'file', 'size', 'uploaded_by', 'uploaded_at']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request:
            validated_data['uploaded_by'] = request.user
        return super().create(validated_data)
