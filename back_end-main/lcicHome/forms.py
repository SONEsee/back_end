from cProfile import label
from email import message
#from socket import fromshare
from tkinter import Widget
from xml.dom import ValidationErr
from django import forms 
from .models import Login, User_Group, Upload_File, Customer_Info_IND ,SegmentType, SType,Upload_Type, EnterpriseInfo
from lcicNews.models import*    
from django.core.validators import RegexValidator
import hashlib
from .validators import validate_file_extension
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django.core.exceptions import ValidationError, ObjectDoesNotExist

# Every letters to LowerCase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
# Every letters to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class addUserForm1(forms.ModelForm):
    check_password = forms.CharField(label='ຢືນຢັນລະຫັດຜ່ານ',max_length=250, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Login
        fields = ['username','password','check_password','nameL','surnameL','nameE','surnameE','is_active','GID','MID']
        labels = {
            'username': 'ຊື່ຜູ້ໃຊ້',
            'password': 'ລະຫັດຜ່ານ',
            'check_password': 'ກວດສອບລະຫັດຜ່ານ',
            'nameL': 'ຊື່ພາສາລາວ',
            'surnameL': 'ນາມສະກຸນພາສາລາວ',
            'nameE': 'ຊື່ພາສາອັງກິດ',
            'surnameE': 'ນາມສະກຸນພາສາອັງກິດ',
            'is_active': 'ສະຖານະ',
            'GID': 'ກຸ່ມຜູ້ໃຊ້',
            'MID': 'ສະມາຊິກ'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','max_length':'250','min_length':'8'}),
            'check_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'nameL': forms.TextInput(attrs={'class': 'form-control'}),
            'surnameL': forms.TextInput(attrs={'class': 'form-control'}),
            'nameE': forms.TextInput(attrs={'class': 'form-control'}),
            'surnameE': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'onoffswitch','id': 'myonoffswitch'}),
            'GID': forms.Select(attrs={'class': 'form-control'}),
            'MID': forms.Select(attrs={'class': 'form-control'}),
        }
        
class addUserForm2(forms.ModelForm):
    
    # Validations
    username = forms.CharField(
        label= 'ຊື່ຜູ້ໃຊ້', min_length=3, max_length= 50,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message= "ກະລຸນາປ້ອນແຕ່ຕົວໜັງສືເທົ່ານັ້້ນ")],
        error_messages= {'required':'ກະລຸນາປ້ອນຊື່ຜູ້ໃຊ້'},
        widget= forms.TextInput(attrs={'placeholder':'ຊື່ຜູ້ໃຊ້'})
        
    )
    
    password = forms.CharField(
        label='ລະຫັດຜ່ານ',max_length=250, min_length=8,
        error_messages= {'required':'ກະລຸນາປ້ອນລະຫັດຜ່ານ'},
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'ລະຫັດຜ່ານ'})
    )
    
    check_password = forms.CharField(
        label='ຢືນຢັນລະຫັດຜ່ານ',max_length=250, min_length=8,
        error_messages= {'required':'ກະລຸນາປ້ອນຢືນຢັນລະຫັດຜ່ານ'},
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'ຢືນຢັນລະຫັດຜ່ານ'})
    )
    
    nameL = forms.CharField(
        label= 'ຊື່ພາສາລາວ', min_length=3, max_length= 50,
        error_messages= {'required':'ກະລຸນາປ້ອນຊື່ພາສາລາວ'},
        widget= forms.TextInput(attrs={'placeholder':'ຊື່ພາສາລາວ'})
        
    )
    surnameL = forms.CharField(
        label= 'ນາມສະກຸນພາສາລາວ', min_length=3, max_length= 50,
        error_messages= {'required':'ກະລຸນາປ້ອນນາມສະກຸນພາສາລາວ'},
        widget= forms.TextInput(attrs={'placeholder':'ນາມສະກຸນພາສາລາວ'})
        
    )
    nameE = forms.CharField(
        label= 'ຊື່ພາສາອັງກິດ', min_length=3, max_length= 50,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message= "ກະລຸນາປ້ອນແຕ່ຕົວໜັງສືເທົ່ານັ້້ນ")],
        error_messages= {'required':'ກະລຸນາປ້ອນຊື່ພາສາອັງກິດ'},
        widget= forms.TextInput(attrs={'placeholder':'ຊື່ພາສາອັງກິດ'})
        
    )
    surnameE = forms.CharField(
        label= 'ນາມສະກຸນພາສາອັງກິດ', min_length=3, max_length= 50,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message= "ກະລຸນາປ້ອນແຕ່ຕົວໜັງສືເທົ່ານັ້້ນ")],
        error_messages= {'required':'ກະລຸນາປ້ອນນາມສະກຸນພາສາອັງກິດ'},
        widget= forms.TextInput(attrs={'placeholder':'ນາມສະກຸນພາສາອັງກິດ'})
        
    )
    
    # GIDD = forms.ChoiceField(
    #     label= 'ກຸ່ມຜູ້ໃຊ້',
    #     error_messages= {'required':'ກະລຸນາເລືອກກຸ່ມຜູ້ໃຊ້'},
    #     widget= forms.Select()
    # )
    # MIDD = forms.ChoiceField(
    #     label= 'ພາກສ່ວນ',
    #     error_messages= {'required':'ກະລຸນາເລືອກພາກສ່ວນ'},
    #     widget= forms.Select()
    # )
    
    GID = forms.ModelChoiceField(
        label= 'ກຸ່ມຜູ້ໃຊ້',
        error_messages= {'required':'ກະລຸນາເລືອກກຸ່ມຜູ້ໃຊ້'},
        queryset=User_Group.objects.all(), initial=0,
        widget= forms.Select(attrs={'placeholder':'ກຸ່ມຜູ້ໃຊ້'})
        )
    MID = forms.ModelChoiceField(
        label= 'ພາກສ່ວນ',
        error_messages= {'required':'ກະລຸນາເລືອກກຸ່ມຜູ້ໃຊ້'},
        queryset=memberInfo.objects.all(), initial=0,
        widget= forms.Select(attrs={'placeholder':'ພາກສ່ວນ'})
        )

    
    class Meta:
        model = Login
        fields =['username','password','check_password','nameL','surnameL','nameE','surnameE','GID','MID']
        labels = {
            'username': 'ຊື່ຜູ້ໃຊ້',
            'password': 'ລະຫັດຜ່ານ',
            'check_password': 'ກວດສອບລະຫັດຜ່ານ',
            'nameL': 'ຊື່ພາສາລາວ',
            'surnameL': 'ນາມສະກຸນພາສາລາວ',
            'nameE': 'ຊື່ພາສາອັງກິດ',
            'surnameE': 'ນາມສະກຸນພາສາອັງກິດ',
            'insertDate': 'ວັນທີເພີ່ມ',
            'updateDate': 'ວັນທີ່ແກ້ໄຂ',
            'GID': 'ກຸ່ມຜູ້ໃຊ້',
            'MID': 'ພາກສ່ວນ'
        }
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'class':'onoffswitch','id': 'myonoffswitch'}),
        }
        
    
    # def clean(self):
    #     cleaned_data = super(addUserForm2, self).clean()
    #     password = cleaned_data.get('password')
    #     check_password = cleaned_data.get('check_password')

    #     if password and check_password:
    #         if password != check_password:
    #             raise forms.ValidationError("The two password fields must match.")
    #         return cleaned_data
    def clean_check_password(self):
        cleaned_data = super(addUserForm2, self).clean()  
        password1 = self.cleaned_data['password']  
        password2 = self.cleaned_data['check_password']
    
        if password1 and password2: 
            if password1 != password2:  
                raise forms.ValidationError("ລະຫັດຜ່ານບໍ່ກົງກັນ")  
            return cleaned_data    
        
        # pw1 = self.cleaned_data.get('password')
        # pw2 = self.cleaned_data.get('check_password')
        # if pw1 and pw2 and pw1 == pw2:
        #     return pw2
        # raise forms.ValidationError("passwords don't match")
            
    def __init__(self, *args, **kwargs):
        super(addUserForm2, self).__init__(*args, **kwargs)
        self.fields['GID'].empty_label = "ເລືອກກຸ່ມຜູ້ໃຊ້"
        self.fields['MID'].empty_label = "ເລືອກພາກສ່ວນ"
    
    # def __init__(self, *args, **kwargs):
    #     super(addUserForm2, self).__init__(*args, **kwargs)
    #     # this is pseudo code but you should get all variants
    #     # then get the product related to each variant
    #     Login = Login.objects.all()
    #     products = [(i.product.id, i.product.name) for i in Login]
    #     self.fields['GID'] = forms.ChoiceField(choices=products)
    
    
class editUserForm(forms.ModelForm):
    
    # Validations
    username = forms.CharField(
    label= 'ຊື່ຜູ້ໃຊ້', min_length=3, max_length= 50,
    validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    message= "ກະລຸນາປ້ອນແຕ່ຕົວໜັງສືເທົ່ານັ້້ນ")],
    error_messages= {'required':'ກະລຸນາປ້ອນຊື່ຜູ້ໃຊ້'},
    widget= forms.TextInput(attrs={'placeholder':'ຊື່ຜູ້ໃຊ້'}) 
    )
        
    password = forms.CharField(
    label='ລະຫັດຜ່ານ',max_length=250, min_length=8,
    error_messages= {'required':'ກະລຸນາປ້ອນລະຫັດຜ່ານ'},
    widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'ລະຫັດຜ່ານ'})
    )
        
    check_password = forms.CharField(
    label='ຢືນຢັນລະຫັດຜ່ານ',max_length=250, min_length=8,
    error_messages= {'required':'ກະລຸນາປ້ອນຢືນຢັນລະຫັດຜ່ານ'},
    widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'ຢືນຢັນລະຫັດຜ່ານ'})
    )
        
    nameL = forms.CharField(
    label= 'ຊື່ພາສາລາວ', min_length=3, max_length= 50,
    error_messages= {'required':'ກະລຸນາປ້ອນຊື່ພາສາລາວ'},
    widget= forms.TextInput(attrs={'placeholder':'ຊື່ພາສາລາວ'})     
    )
    surnameL = forms.CharField(
    label= 'ນາມສະກຸນພາສາລາວ', min_length=3, max_length= 50,
    error_messages= {'required':'ກະລຸນາປ້ອນນາມສະກຸນພາສາລາວ'},
    widget= forms.TextInput(attrs={'placeholder':'ນາມສະກຸນພາສາລາວ'})    
    )
    nameE = forms.CharField(
    label= 'ຊື່ພາສາອັງກິດ', min_length=3, max_length= 50,
    validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    message= "ກະລຸນາປ້ອນແຕ່ຕົວໜັງສືເທົ່ານັ້້ນ")],
    error_messages= {'required':'ກະລຸນາປ້ອນຊື່ພາສາອັງກິດ'},
    widget= forms.TextInput(attrs={'placeholder':'ຊື່ພາສາອັງກິດ'})
            
    )
    surnameE = forms.CharField(
    label= 'ນາມສະກຸນພາສາອັງກິດ', min_length=3, max_length= 50,
    validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    message= "ກະລຸນາປ້ອນແຕ່ຕົວໜັງສືເທົ່ານັ້້ນ")],
    error_messages= {'required':'ກະລຸນາປ້ອນນາມສະກຸນພາສາອັງກິດ'},
    widget= forms.TextInput(attrs={'placeholder':'ນາມສະກຸນພາສາອັງກິດ'})
    )
        
    GID = forms.ModelChoiceField(
    label= 'ກຸ່ມຜູ້ໃຊ້',
    error_messages= {'required':'ກະລຸນາເລືອກກຸ່ມຜູ້ໃຊ້'},
    queryset=User_Group.objects.all(), initial=0,
    widget= forms.Select(attrs={'placeholder':'ກຸ່ມຜູ້ໃຊ້'})
            )
    MID = forms.ModelChoiceField(
    label= 'ພາກສ່ວນ',
    error_messages= {'required':'ກະລຸນາເລືອກພາກສ່ວນ'},
    queryset=memberInfo.objects.all(), initial=0,
    widget= forms.Select(attrs={'placeholder':'ພາກສ່ວນ'})
    )    
    
    STATUS = [('True','Active'),('False','Inactive')]
    is_active = forms.CharField(
        required=False,
        label= 'ສະຖານະ:',
        widget= forms.RadioSelect(choices=STATUS)
    )
    
    class Meta:
        model = Login
        fields =['username','password','check_password','nameL','surnameL','nameE','surnameE','GID','MID', 'is_active']
        labels = {
            'username': 'ຊື່ຜູ້ໃຊ້',
            'password': 'ລະຫັດຜ່ານ',
            'check_password': 'ກວດສອບລະຫັດຜ່ານ',
            'nameL': 'ຊື່ພາສາລາວ',
            'surnameL': 'ນາມສະກຸນພາສາລາວ',
            'nameE': 'ຊື່ພາສາອັງກິດ',
            'surnameE': 'ນາມສະກຸນພາສາອັງກິດ',
            'insertDate': 'ວັນທີເພີ່ມ',
            'updateDate': 'ວັນທີ່ແກ້ໄຂ',
            'GID': 'ກຸ່ມຜູ້ໃຊ້',
            'MID': 'ພາກສ່ວນ',
            'is_active':'ສະຖານະ'
        }
        
    
    # def clean(self):
    #     cleaned_data = super(addUserForm2, self).clean()
    #     password = cleaned_data.get('password')
    #     check_password = cleaned_data.get('check_password')

    #     if password and check_password:
    #         if password != check_password:
    #             raise forms.ValidationError("The two password fields must match.")
    #         return cleaned_data
    def clean_check_password(self):
        cleaned_data = super(editUserForm, self).clean()  
        password1 = self.cleaned_data['password']  
        password2 = self.cleaned_data['check_password']
        if password1 and password2: 
            if password1 != password2:  
                raise forms.ValidationError("ລະຫັດຜ່ານບໍ່ກົງກັນ")  
            return cleaned_data    
        
        # pw1 = self.cleaned_data.get('password')
        # pw2 = self.cleaned_data.get('check_password')
        # if pw1 and pw2 and pw1 == pw2:
        #     return pw2
        # raise forms.ValidationError("passwords don't match")
            
    def __init__(self, *args, **kwargs):
        super(editUserForm, self).__init__(*args, **kwargs)
        self.fields['GID'].empty_label = "ເລືອກກຸ່ມຜູ້ໃຊ້"
        self.fields['MID'].empty_label = "ເລືອກພາກສ່ວນ"
    
    # def __init__(self, *args, **kwargs):
    #     super(addUserForm2, self).__init__(*args, **kwargs)
    #     # this is pseudo code but you should get all variants
    #     # then get the product related to each variant
    #     Login = Login.objects.all()
    #     products = [(i.product.id, i.product.name) for i in Login]
    #     self.fields['GID'] = forms.ChoiceField(choices=products)
    
class showUploadForm(forms.ModelForm):
    MID = forms.ModelChoiceField(
    label= 'ສະມາຊິກ',
    queryset=memberInfo.objects.all(), initial=0,
    widget= forms.Select(attrs={'placeholder':'ສະມາຊິກ'})
    )
    status = forms.ModelChoiceField(
        label= 'ສະຖານະ',
        queryset=Upload_File.objects.values('status'), initial=0,
        widget= forms.Select(attrs={'placeholder':'ສະຖານະ'})
    )
    period = forms.ModelChoiceField(
        label='ຂໍ້ມູນປະຈຳເດືອນ',
        queryset=Upload_File.objects.values('period'), initial=0,
        widget= forms.Select(attrs={'placeholder':'ຂໍ້ມູນປະຈຳເດືອນ'})
    )
    
    class Meta:
        model = Upload_File
        fields =['MID']
        labels = {
            'MID': 'ສະມາຊິກ',
            'status': 'ສະຖານະ',
            'period': 'ຂໍ້ມູນປະຈຳເດືອນ'
        }
        
    def __init__(self, *args, **kwargs):
        super(showUploadForm, self).__init__(*args, **kwargs)
        self.fields['MID'].empty_label = "ທັງໝົດ"
        self.fields['status'].empty_label = "ທັງໝົດ"
        self.fields['period'].empty_label = "ທັງໝົດ"

class uploadForm(forms.ModelForm):

    SType_id =(
    ('A1','ສຳລັບຜູ້ກູ້ຢືມທີ່ເປັນບຸກຄົນ ແລະ ຜູ້ກູ້ຢືມເປັນລາຍກຸ່ມ-(A1)'),
    ('A2','ສຳລັບຜູ້ກູ້ຢືມທີ່ເປັນວິສາຫະກິດ-(A2)'),
    ('A3','ຜູ້ມີລາຍເຊັນຮ່ວມກັນ-(A3)'),
    ('A4','ລາຍລະອຽດກ່ຽວກັບທີ່ຢູ່ອາໃສ-(A4)'),
    ('A5','ລາຍລະອຽດກ່ຽວກັບຂໍ້ມູນຕິດຕໍ່ຂອງລູກຄ້າ-(A5)'),
    ('B1','ລາຍລະອຽດຂອງເງິນກູ້ຢືມ-(B1)'),
    ('C1','ການສະຫລຸບຂໍ້ມູນຂອງຫລັກຊັບຄ້ຳປະກັນ-(C1)'),
    ('C2.1','ອາຄານ/ ອາຄານ + ທີ່ດິນ/ ເຮືອນ/ເຮືອນ+ທີ່ດິນ/ ທີ່ດິນ-(C2.1)'),
    ('C2.2',' ເງິນໃນບັນຊີ/ເອກະສານມີຄ່າ-(C2.2)'),
    ('C2.3','ເຄື່ອງຈັກ ແລະ ອຸປະກອນຕ່າງໆ-(C2.3)'),
    ('C2.4','ໂຄງການ-(C2.4)'),
    ('C2.5','ຍານພາຫະນະ-(C2.5)'),
    ('C2.6',' ຜູ້ຄ້ຳປະກັນ-(C2.6)'),
    ('C2.7','ທອງ ແລະ ເງິນ-(C2.7)'),
)
    fileUpload = forms.FileField(
        label='ການນຳສົ່ງຂໍ້ມູນ - ການນຳສົ່ງຂໍ້ມູນໃໝ່',
        required=True,
        error_messages={'required':'ກະລຸນາເລືອກໄຟຣ'},
        validators=[validate_file_extension],
        widget= forms.ClearableFileInput(attrs={'placeholder':'ເລືອກໄຟຣ໌'})
        )
    SType = forms.ModelChoiceField(
        label ='ປະເພດຂໍ້ມູນ',
        queryset=SType.objects.all(), initial=0,
        error_messages={'required':'ກະລຸນາເລືອກປະເພດຂໍ້ມູນ'},
        widget= forms.Select(attrs={'class':'form-control'})
    )
    UploadType = [(1,'ປະຈຳວັນ'),(2,'ປະຈຳເດືອນ')]
    UType = forms.ModelChoiceField(
        label='ປະເພດນຳສົ່ງ',
        queryset=Upload_Type.objects.all(), initial=0,
        widget= forms.RadioSelect(attrs={'class':'form-control'}),
        error_messages={'required':'ກະລຸນາເລືອກປະເພດນຳສົ່ງຂໍ້ມູນ'},
        )
        
    class Meta:
        model = Upload_File
        fields =['fileUpload','SType','UType']
        labels = {
            'fileUpload': 'ການນຳສົ່ງຂໍ້ມູນ - ການນຳສົ່ງຂໍ້ມູນໃໝ່',
            'SType': 'ປະເພດຂໍ້ມູນ',
        }
    def __init__(self, *args, **kwargs):
        super(uploadForm, self).__init__(*args, **kwargs)
        self.fields["SType"].choices = [("","ເລຶອກປະເພດຂໍ້ມູນ"),] + list(self.fields["SType"].choices)[0:]

class searchIndividualForm(forms.ModelForm):
    ind_lao_name = forms.CharField(
        label= 'ຊື່ພາສາລາວ', min_length=3, max_length= 50,
        error_messages= {'required':'ກະລຸນາປ້ອນຊື່ພາສາລາວ'},
        widget= forms.TextInput(attrs={'placeholder':'ຊື່ພາສາລາວ'})
    )
    ind_lao_surname = forms.CharField(
        label='ນາມສະກຸນພາສາລາວ', min_length=3, max_length=50,
        error_messages={'required':'ກະລຸນາປ້ອນນາມສະກຸນພາສາລາວ'},
        widget= forms.TextInput(attrs={'placeholder':'ນາມສະກຸນພາສາລາວ'})
    )
    ind_name = forms.CharField(
        label= 'ຊື່ພາສາອັງກິດ', min_length=3, max_length= 50,
        error_messages= {'required':'ກະລຸນາປ້ອນຊື່ພາສາອັງກິດ'},
        widget= forms.TextInput(attrs={'placeholder':'ຊື່ພາສາອັງກິດ'})
    )
    ind_surname = forms.CharField(
        label='ນາມສະກຸນພາສາອັງກິດ', min_length=3, max_length=50,
        error_messages={'required':'ກະລຸນາປ້ອນຊື່ນາມສະກຸນພາສາອັງກິດ'},
        widget= forms.TextInput(attrs={'placeholder':'ນາມສະກຸນພາສາອັງກິດ'})
    )
    customerid = forms.CharField(
        label = 'ລະຫັດລູກຄ້າ', min_length=20, max_length=50,
        error_messages={'required':'ກະລຸນາປ້ອນລະຫັດລູກຄ້າ'},
        widget = forms.TextInput(attrs=
        {'placeholder':'ລະຫັດລູກຄ້າ'})
    )
    class Meta:
        model = Customer_Info_IND
        fields =['ind_lao_name']
        labels = {
            'ind_lao_name': 'ຊື່ພາສາລາວ',
            'ind_lao_surname': 'ນາມສະກຸນພາສາລາວ',
            'ind_name': 'ຊື່ພາສາອັງກິດ',
            'ind_surname': 'ນາມສະກຸນພາສາອັງກິດ',
            'customerid': 'ລະຫັດລູກຄ້າ'
        }
              
class SearchEnterpise(forms.ModelForm):
    enterprise_id = forms.CharField(
        label = 'ລະຫັດວິສະຫາກິດ', min_length=4, max_length=50,
        error_messages={'required':'ກະລຸນາປ້ອນລະຫັດວິສະຫາກິດ'},
        widget = forms.TextInput(attrs= 
        {'placeholder':'ລະຫັດວິສະຫາກິດ'}))
        
    lcic_id = forms.CharField(
        label = 'ລະຫັດຂສລ', min_length=4, max_length=50,
        error_messages={'required':'ກະລຸນາປ້ອນລະຫັດຂສລ'},
        widget = forms.TextInput(attrs=
        {'placeholder':'ລະຫັດຂສລ'}))

    
    class Meta:
        model = EnterpriseInfo
        fields =['enterprise_id']
        labels = {
            'enterprise_id': 'ລະຫັດວິສະຫາກິດ',
            'lcic_id': 'ລະຫັດຂສລ'
        }
        
    # def clean_enterprise_id(self):
    #     enterprise_id = self.cleaned_data.get('enterprise_id')
    #     if not enterprise_id.isalpha():
    #         raise ValidationError('ກະລຸນາປ້ອນຕົວອັກສອນໃຫມ່')
    #     return enterprise_id

    # def clean_lcic_id(self):
    #     lcic_id = self.cleaned_data.get('lcic_id')
    #     if not lcic_id.isalpha():
    #         raise ValidationError('ກະລຸນາປ້ອນຕົວອັກສອນໃຫມ່')
    #     return lcic_id
    
        
class SearchForm(forms.Form):
    enterprise_id = forms.CharField(label='ລະຫັດວິສາຫະກິດ', required=False)
    lcic_id = forms.CharField(label='ລະຫັດຂສລ', required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('enterprise_id', css_class='col-6'),
                Column('lcic_id', css_class='col-6'),
            ),
            Row(
                Column('submit', css_class='col-6'),
                Column('cancel', css_class='col-6'),
            ),
        )

    def clean(self):
        cleaned_data = super().clean()
        enterprise_id = cleaned_data.get('enterprise_id')
        lcic_id = cleaned_data.get('lcic_id')

        # Perform custom validation
        
        if not enterprise_id and not lcic_id:
            raise ValidationError("ກະລຸນາໃສລະຫັດວິສາຫະກິດ ເເລະ ລະຫັດຂສລ")

        # Add more specific validation if needed

        return cleaned_data
