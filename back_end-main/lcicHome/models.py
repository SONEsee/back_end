# from sre_parse import Verbose
from tabnanny import verbose
from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.html import format_html
from lcicNews.models import*
from .validators import validate_file_extension
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from datetime import timedelta
import logging
import binascii
import os
class H_imageBar(models.Model):
    code =models.CharField(max_length=20,unique=True)
    nameL = models.CharField(max_length=500)
    nameE = models.CharField(max_length=500)
    detailL = models.TextField(null=True,blank=True)
    detailE = models.TextField(null=True,blank=True)
    imageBar = models.FileField(upload_to='upload', null=True,blank=True)
    imageS = models.FileField(upload_to='UploadHome', null=True,blank=True)
    published = models.BooleanField(default=False)
    class Meta:
        ordering =['-id']
        verbose_name_plural='ImageSlidBar'
    def _str_(self):
        return self.code
    def ImageB(self):
        if self.imageBar:
            return format_html('<img src="'+ self.imageBar.url +'" height="50px">')
        return ''
    ImageB.allow_tags= True
    def imageSlidMain(self):
        if self.imageS:
            return format_html('<img src="'+ self.imageS.url +'" height="50px">')
        return ''
    imageSlidMain.allow_tags= True


class H_proType(models.Model):
    nameL = models.CharField(max_length=100)
    nameE = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='proType'
    def _str_(seft):
        return seft.nameL

class H_productInfo(models.Model):
    code = models.CharField(max_length=10,unique=True)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    nameL = models.CharField( max_length=250)
    nameE = models.CharField(max_length=250)
    descE = models.TextField(null=True,blank=True)
    descL = models.TextField(null=True,blank =True )
    price = models.IntegerField (default=0)
    proType = models.ForeignKey(H_proType, null=True,blank=True, on_delete=models.CASCADE)
    pimage = models.FileField(upload_to='uploadProducts',null=True,blank=True)
    pFiles = models.FileField(upload_to='uploadProducts',null=True,blank=True)
    published = models.BooleanField(default=False)
    insertDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateDate = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        ordering=['id']
        verbose_name_plural='ProductInfo'
    def _str_(self):
        return self.nameL
    def pshowImage(self):
        if self.pimage:
            return format_html('<img src="'+ self.pimage.url +'" height="40px" >')
        return ''
    pshowImage.allow_tags =True
    def pshowFiles(self):
        if self.pFiles:
            return format_html('<img src="'+ self.pFiles.url +'" height="40px" >')
        return ''    
    pshowFiles.allow_tags =True
    

class H_newsType(models.Model):
    nameL = models.CharField(max_length=100)
    nameE = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='newsType'
    def _str_(seft):
        return seft.nameL

class H_userInfo(models.Model):
    code = models.CharField(max_length=50)
    nameL = models.CharField(max_length=100)
    nameE = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='userInfo'
    def _str_(seft):
        return seft.nameL

class H_newsInfo(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nameE = models.CharField(max_length=100, null = True,blank=True)
    nameL = models.CharField(max_length=100, null= True, blank= True)
    descE  = models.TextField(null=True,blank=True)
    descL = models.TextField(null=True,blank =True )
    newsType = models.ForeignKey(H_newsType, null=True, blank=True ,on_delete=models.CASCADE)
    userInfo = models.ManyToManyField(H_userInfo,blank=True)
    nimage = models.FileField(upload_to='uploadNews',null=True,blank=True)
    nFilesL = models.FileField(upload_to='uploadNewsFlils/uploadNewsFlilsL',null=True,blank=True)
    nFilesE = models.FileField(upload_to='uploadNewsFlils/uploadNewsFlilsE',null=True,blank=True)
    published = models.BooleanField(default=False)
    insertDate = models.DateTimeField(auto_now_add = True)
    updateDate = models.DateTimeField(auto_now = True)
    class Meta:
        ordering =['-id']
        verbose_name_plural='newsInfo'
    def _str_(self):
        return self.nameL
    def showImage(self):
        if self.nimage:
            return format_html('<img src="'+ self.nimage.url +'" height="40px" >')
        return ''
    showImage.allow_tags = True

class H_newsCommand(models.Model):
    code = models.ForeignKey(H_newsInfo,on_delete=models.CASCADE)
    commandL = models.CharField(max_length=50)
    commandE= models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    class Meta:
        ordering =['-id']
        verbose_name_plural='news'
    def _str_(self):
        return self.commandL
    
class H_Lang(models.Model):
    id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Trans_LA = models.TextField(null=True,blank=True)
    Trans_EN = models.TextField(null=True,blank=True)
    class Meta:
        #ordering= ('id')
        verbose_name_plural='H_Lang'
    def _str_(self):
        return self.Trans_LA
    
    
class User_Login(models.Model):
    id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    UserName = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)


class Group_User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=150)
    
    
class User_Group(models.Model):
    GID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameL = models.CharField(max_length=150)
    nameE = models.CharField(max_length=150)
    class Meta:
        # ordering= ('GID')
        verbose_name_plural='GroupUser'
    def _str_(self):
        return self.nameL
    
    
class Menu(models.Model):
    MID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameL = models.CharField(max_length=150)
    nameE = models.CharField(max_length=150)
    class Meta:
        # ordering=('MID')
        verbose_name_plural='Nav_Menu'
    def _str_(self):
        return self.nameL

class SubMenu(models.Model):
    SMID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    MID = models.ForeignKey(Menu,  null=True, blank=True ,on_delete=models.CASCADE)
    nameL = models.CharField(max_length=150)
    nameE = models.CharField(max_length=150)
    class Meta:
        # ordering='SMID'
        verbose_name_plural='Nav_Submenu'
    def _str_(self):
        return self.nameL
    
class GroupSubMenu(models.Model):
    GSMID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    GID = models.ForeignKey(User_Group, null=True, blank=True , on_delete=models.CASCADE)
    SMID = models.ForeignKey(SubMenu, null=True, blank=True , on_delete=models.CASCADE)
    insertDate = models.DateTimeField(auto_now_add = True)
    updateDate = models.DateTimeField(auto_now = True)
    class Meta:
        # ordering='GSMID'
        verbose_name_plural='GroupSubMenu'

# class Login(models.Model):
#     UID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     MID = models.ForeignKey(memberInfo, related_name='memberInfo', null=True, blank=True, on_delete=models.CASCADE)
#     GID = models.ForeignKey(User_Group, null=True, blank=True , on_delete=models.CASCADE)
#     username = models.CharField(max_length=150)
#     password = models.CharField(max_length=150)
#     nameL = models.CharField(max_length=150)
#     nameE = models.CharField(max_length=150)
#     surnameL = models.CharField(max_length=150)
#     surnameE = models.CharField(max_length=150)
#     insertDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
#     updateDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
#     is_active = models.BooleanField(default=True)
    
    
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return 

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)
     

class Login(AbstractBaseUser):
    UID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    MID = models.ForeignKey(memberInfo, related_name='memberInfo', null=True, blank=True, on_delete=models.CASCADE)
    GID = models.ForeignKey(User_Group, null=True, blank=True , on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    nameL = models.CharField(max_length=150)
    nameE = models.CharField(max_length=150)
    surnameL = models.CharField(max_length=150)
    surnameE = models.CharField(max_length=150)
    insertDate = models.DateTimeField(auto_now_add=True, blank=True)
    updateDate = models.DateTimeField(auto_now=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()
    
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    
class bank_bnk(models.Model):
    bnk_sys_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    bnk_code = models.CharField(max_length=10,null=False, blank=False)
    bnk_short_form = models.CharField(max_length=10)
    bnk_name = models.CharField(max_length=100)
    bnk_lao_name = models.TextField()
    bnk_insert_date = models.DateField(null=True, blank=True)
    bnk_type = models.IntegerField()
    
    
class bank_branch(models.Model):
    branch_sys_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    bnk_code = models.CharField(max_length=10,null=False, blank=False)
    branch_id = models.CharField(max_length=15,null=False, blank=False)
    branch_name = models.CharField(max_length=50)
    Vill = models.CharField(max_length=50)
    Dis = models.CharField(max_length=50)
    Province = models.CharField(max_length=50)


class CustomerWater(models.Model):
    ID = models.BigAutoField(auto_created= True, primary_key=True, serialize=False, verbose_name='ID')
    CustomerID = models.CharField(max_length=150, null=False, blank=True)
    CompanyName = models.CharField(max_length=250,null=True)
    Name = models.CharField(max_length=150)
    Surname = models.CharField(max_length=150)
    NationalID = models.CharField(max_length=150,null=True)
    Passport = models.CharField(max_length=150,null=True)
    Address = models.CharField(max_length=150,null=False)
    districtInfo = models.CharField(max_length=150, null=False, blank=True)
    provInfo = models.CharField(max_length=150, null=False, blank=True)
    Tel = models.CharField(max_length=150)
    Email = models.EmailField(max_length=254)
    ConsumerType = models.CharField(max_length=150)
    RegisDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    
    # @classmethod
    # def create(cls, **kwargs):
    #     CustomerWater = cls.objects.create(
    #         ID=kwargs['ID'],
    #         CustomerID=kwargs['CustomerID'],
    #         CompanyName=kwargs['CompanyName'],
    #         Name=kwargs['Name'],
    #         Surname=kwargs['Surname'],
    #         NationalID=kwargs['NationalID'],
    #         Passport=kwargs['Passport'],
    #         Address=kwargs['Address'],
    #         districtInfo=kwargs['districtInfo'],
    #         provInfo=kwargs['provInfo'],
    #         Tel=kwargs['Tel'],
    #         Email=kwargs['Email'],
    #         ConsumerType=kwargs['ConsumerType'],
    #         RegisDate=kwargs['RegisDate'],
            
    #     )
    #     # for ID in kwargs['ID']:
    #     #     genre, created = CustomerWater.objects.get_or_create(ID=ID)
    #     #     CustomerWater.genre.add(genre)
    #     return CustomerWater
    class Meta:
        verbose_name_plural='CustomerWater'
    def _str_(seft):
        return seft.Name
    
    
    
    
class BillWater(models.Model):
    BillID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    CustomerID = models.CharField(max_length=150, null=False, blank=True)
    SupplyType = models.CharField(max_length=150)
    Outstanding = models.DecimalField(max_digits=100,decimal_places=2)
    BasicTax = models.DecimalField(max_digits=100,decimal_places=2)
    PayAmount = models.DecimalField(max_digits=100,decimal_places=2)
    PaymentID = models.CharField(max_length=150)
    PayType = models.CharField(max_length=150)
    BillOfMonth = models.CharField(max_length=150)
    DateOfIssue = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    PaymentDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    districtInfo = models.CharField(max_length=150, null=False, blank=True)
    provInfo = models.CharField(max_length=150, null=False, blank=True)
    
class SegmentType(models.Model):
    SType = models.CharField(max_length=150, null=False, auto_created= False, primary_key=True, serialize=False, verbose_name='ID')
    nameL = models.CharField(max_length=150, null=False, blank=True)
    nameE = models.CharField(max_length=150, null=False, blank=True)
    class meta:
        verbose_name_plural ='SegmentType'
    def _str_(self):
        return self.SType
    
    
class SType(models.Model):
    SType = models.CharField(max_length=150, null=False)
    nameL = models.CharField(max_length=150, null=False, blank=True)
    nameE = models.CharField(max_length=150, null=False, blank=True)
    class meta:
        ordering=['SType']
        verbose_name_plural ='SegmentType'
    def _str_(self):
        return self.nameL
# class Uploads(models.Model):
#     FID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     MID = models.ForeignKey(memberInfo, null=True, blank=True, on_delete=models.CASCADE)
#     GID = models.ForeignKey(User_Group, null=True, blank=True , on_delete=models.CASCADE)
#     SType = models.ForeignKey(SegmentType, null=True, blank=True , on_delete=models.CASCADE)
#     fileName = models.CharField(max_length=255)
#     fileUpload = models.FileField()
#     fileSize = models.CharField(max_length=255)
#     path = models.CharField(max_length=255)
#     insertDate = models.DateTimeField(auto_now_add=True, blank=True)
#     updateDate = models.DateTimeField(auto_now_add=True, blank=True)
#     period = models.CharField(max_length=150)
#     status = models.CharField(max_length=150)
#     status_upload = models.CharField(max_length=150)
#     uploadType = models.CharField(max_length=10)

SType_id =(
    ('A1','ສຳລັບຜູ້ກູ້ຢືມທີ່ເປັນບຸກຄົນ ແລະ ຜູ້ກູ້ຢືມເປັນລາຍກຸ່ມ'),
    ('A2','ສຳລັບຜູ້ກູ້ຢືມທີ່ເປັນວິສາຫະກິດ'),
    ('A3','ຜູ້ມີລາຍເຊັນຮ່ວມກັນ'),
    ('A4','ລາຍລະອຽດກ່ຽວກັບທີ່ຢູ່ອາໃສ'),
    ('A5','ລາຍລະອຽດກ່ຽວກັບຂໍ້ມູນຕິດຕໍ່ຂອງລູກຄ້າ'),
    ('B1','ລາຍລະອຽດຂອງເງິນກູ້ຢືມ'),
    ('C1','ການສະຫລຸບຂໍ້ມູນຂອງຫລັກຊັບຄ້ຳປະກັນ'),
    ('C2.1','ອາຄານ/ ອາຄານ + ທີ່ດິນ/ ເຮືອນ/ເຮືອນ+ທີ່ດິນ/ ທີ່ດິນ'),
    ('C2.2',' ເງິນໃນບັນຊີ/ເອກະສານມີຄ່າ'),
    ('C2.3','ເຄື່ອງຈັກ ແລະ ອຸປະກອນຕ່າງໆ'),
    ('C2.4','ໂຄງການ'),
    ('C2.5','ຍານພາຫະນະ'),
    ('C2.6',' ຜູ້ຄ້ຳປະກັນ'),
    ('C2.7','ທອງ ແລະ ເງິນ'),
)

class Upload_Type(models.Model):
    UType = models.CharField(max_length=3)
    nameL = models.CharField(max_length=50)
    nameE = models.CharField(max_length=50)
    class meta:
        ordering=['UType']
        verbose_name_plural = 'UploadType'
    def _str_(self):
        return self.nameL

class Upload_File(models.Model):
    # FID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')  id = models.AutoField(primary_key=True)
    FID = models.AutoField(primary_key=True)
    MID = models.ForeignKey(memberInfo, null=True, blank=True, on_delete=models.CASCADE)
    GID = models.ForeignKey(User_Group, null=True, blank=True , on_delete=models.CASCADE)
    SType = models.ForeignKey(SType, null=True, blank=True , on_delete=models.CASCADE)
    UType = models.ForeignKey(Upload_Type, null=True, blank=True, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=255)
    fileUpload = models.FileField(upload_to="uploadFiles/")
    fileSize = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    insertDate = models.DateTimeField(auto_now_add=True, blank=True)
    updateDate = models.DateTimeField(auto_now_add=True, blank=True)
    period = models.CharField(max_length=150)
    status = models.CharField(max_length=150)     
    status_upload = models.CharField(max_length=150)
    FileType = models.CharField(max_length=10)     
    def __str__(self):
        return self.title    



class Customer_IND_Keys(models.Model):
    mm_ind_sys_id = models.IntegerField(default=0)
    bnk_code = models.CharField(max_length=10)
    branchcode = models.CharField(max_length=30)
    customerid = models.CharField(max_length=30)
    ind_national_id = models.CharField(max_length=30)
    ind_national_id_date = models.DateField()
    ind_passport = models.CharField(max_length=30)
    ind_passport_date = models.DateField()
    ind_familybook = models.CharField(max_length=30)
    ind_familybook_prov_code = models.CharField(max_length=20)
    ind_familybook_date = models.DateField()
    
    
    
    
class Customer_Info_IND(models.Model):
    mm_ind_sys_id = models.IntegerField(default=0, null=True)
    bnk_code = models.CharField(max_length=10)
    branchcode = models.CharField(max_length=30)
    customerid = models.CharField(max_length=30)
    ind_birth_date = models.DateField()
    ind_name = models.CharField(max_length=100)
    ind_second_name = models.CharField(max_length=30)
    ind_surname = models.CharField(max_length=100)
    ind_lao_name = models.TextField()
    ind_lao_surname = models.TextField()
    ind_old_surname = models.CharField(max_length=30, null=True)
    ind_lao_old_surname = models.TextField()
    ind_nationality = models.CharField(max_length=3)
    ind_gender = models.CharField(max_length=1)
    ind_civil_status = models.CharField(max_length=10, null=True)
    ind_insert_date = models.DateTimeField(blank=True)
    ind_update_date = models.DateTimeField(blank=True)
    mm_action_date = models.DateTimeField(blank=True, null=True)
    blk_sys_id = models.IntegerField(default=0)
    mm_status = models.CharField(max_length=1, null=True)

    
class Customer_Keys_IND(models.Model):
    mm_ind_sys_id = models.IntegerField(default=0)
    bnk_code = models.CharField(max_length=10)
    branchcode = models.CharField(max_length=30)
    customerid = models.CharField(max_length=30)
    CKCode = models.CharField(max_length=30)
    RegisDate = models.DateField()
    VillCode = models.CharField(max_length=10)
    KType = models.CharField(max_length=1)
    status = models.CharField(max_length=100)
    insert_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)
    userid = models.CharField(max_length=30)
    
    
class Lcic_Info(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    mm_ind_sys_id = models.IntegerField(default=0)
    insert_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)
    userid = models.CharField(max_length=30)
    status = models.CharField(max_length=100)
    
class Customer_Info_IND_ERRORS(models.Model):
    mm_ind_sys_id = models.IntegerField(default=0, null=True)
    bnk_code = models.CharField(max_length=10)
    branchcode = models.CharField(max_length=30)
    customerid = models.CharField(max_length=30)
    ind_birth_date = models.DateField()
    ind_name = models.CharField(max_length=100)
    ind_second_name = models.CharField(max_length=30)
    ind_surname = models.CharField(max_length=100)
    ind_lao_name = models.TextField()
    ind_lao_surname = models.TextField()
    ind_old_surname = models.CharField(max_length=30, null=True)
    ind_lao_old_surname = models.TextField()
    ind_nationality = models.CharField(max_length=3)
    ind_gender = models.CharField(max_length=1)
    ind_civil_status = models.CharField(max_length=10, null=True)
    ind_insert_date = models.DateTimeField(blank=True)
    ind_update_date = models.DateTimeField(blank=True)
    mm_action_date = models.DateTimeField(blank=True, null=True)
    blk_sys_id = models.IntegerField(default=0)
    mm_status = models.CharField(max_length=1, null=True)
    

  
  
from django.core.exceptions import ValidationError

class B1_Monthly(models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    lcicID = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    com_enterprise_code = models.CharField(max_length=100)
    segmentType = models.CharField(max_length=100)
    bnk_code = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    branch_id = models.CharField(max_length=100)
    lon_sys_id = models.CharField(max_length=100)
    loan_id = models.CharField(max_length=100)
    lon_open_date = models.DateField(null=True)
    lon_exp_date = models.DateField(null=True)
    lon_ext_date = models.DateField(null=True)
    lon_int_rate = models.FloatField(default=0)
    lon_purpose_code = models.CharField(max_length=100)
    lon_credit_line = models.FloatField(default=0)
    lon_currency_code = models.CharField(max_length=100)
    lon_outstanding_balance = models.FloatField(default=0)
    lon_account_no = models.CharField(max_length=100)
    lon_no_days_slow = models.IntegerField(default=0)
    lon_class = models.CharField(max_length=100)
    lon_type = models.CharField(max_length=100)
    lon_term = models.CharField(max_length=100)
    lon_status = models.CharField(max_length=100)
    lon_insert_date = models.DateTimeField(null=True)
    lon_update_date = models.DateTimeField(null=True)
    lon_applied_date = models.DateTimeField(null=True)
    is_disputed = models.BigIntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        self.lon_no_days_slow = self.lon_no_days_slow or 0
        self.is_disputed = self.is_disputed or 0
        
        if not isinstance(self.lon_no_days_slow, int):
            raise ValidationError("lon_no_days_slow must be an integer")
        if not isinstance(self.is_disputed, int):
            raise ValidationError("is_disputed must be an integer")
            
        super().save(*args, **kwargs)

class B_Data_is_damaged(models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    lcicID = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    lcicID_error = models.CharField(max_length=100)
    com_enterprise_code_error = models.CharField(max_length=100)
    com_enterprise_code = models.CharField(max_length=100)
    segmentType = models.CharField(max_length=100)
    bnk_code = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    branch_id = models.CharField(max_length=100)
    lon_sys_id = models.CharField(max_length=100)
    loan_id = models.CharField(max_length=100)
    lon_open_date = models.DateField(null=True)
    lon_exp_date = models.DateField(null=True)
    lon_ext_date = models.DateField(null=True)
    lon_int_rate = models.FloatField(default=0)
    lon_purpose_code = models.CharField(max_length=100)
    lon_credit_line = models.FloatField(default=0)
    lon_currency_code = models.CharField(max_length=100)
    lon_outstanding_balance = models.FloatField(default=0)
    lon_account_no = models.CharField(max_length=100)
    lon_no_days_slow = models.IntegerField(default=0)
    lon_class = models.CharField(max_length=100)
    lon_type = models.CharField(max_length=100)
    lon_term = models.CharField(max_length=100)
    lon_status = models.CharField(max_length=100)
    lon_insert_date = models.DateTimeField(null=True)
    lon_update_date = models.DateTimeField(null=True)
    lon_applied_date = models.DateTimeField(null=True)
    is_disputed = models.BigIntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        self.lon_no_days_slow = self.lon_no_days_slow or 0
        self.is_disputed = self.is_disputed or 0
        
        if not isinstance(self.lon_no_days_slow, int):
            raise ValidationError("lon_no_days_slow must be an integer")
        if not isinstance(self.is_disputed, int):
            raise ValidationError("is_disputed must be an integer")
            
        super().save(*args, **kwargs)

class data_edit(models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    lcicID = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    com_enterprise_code = models.CharField(max_length=100)
    segmentType = models.CharField(max_length=100)
    bnk_code = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    branch_id = models.CharField(max_length=100)
    lon_sys_id = models.CharField(max_length=100)
    loan_id = models.CharField(max_length=100)
    lon_open_date = models.DateField(null=True)
    lon_exp_date = models.DateField(null=True)
    lon_ext_date = models.DateField(null=True)
    lon_int_rate = models.FloatField(default=0)
    lon_purpose_code = models.CharField(max_length=100)
    lon_credit_line = models.FloatField(default=0)
    lon_currency_code = models.CharField(max_length=100)
    lon_outstanding_balance = models.FloatField(default=0)
    lon_account_no = models.CharField(max_length=100)
    lon_no_days_slow = models.IntegerField(default=0)
    lon_class = models.CharField(max_length=100)
    lon_type = models.CharField(max_length=100)
    lon_term = models.CharField(max_length=100)
    lon_status = models.CharField(max_length=100)
    lon_insert_date = models.DateTimeField(null=True)
    lon_update_date = models.DateTimeField(null=True)
    lon_applied_date = models.DateTimeField(null=True)
    is_disputed = models.BigIntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        self.lon_no_days_slow = self.lon_no_days_slow or 0
        self.is_disputed = self.is_disputed or 0
        
        if not isinstance(self.lon_no_days_slow, int):
            raise ValidationError("lon_no_days_slow must be an integer")
        if not isinstance(self.is_disputed, int):
            raise ValidationError("is_disputed must be an integer")
            
        super().save(*args, **kwargs)

class B1(models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100,default='default_value')
    lcicID = models.CharField(max_length=255, blank=True, null=True)
    com_enterprise_code = models.CharField(max_length=255, blank=True, null=True)
    period = models.CharField(max_length=100)
    segmentType = models.CharField(max_length=255, blank=True, null=True)
    bnk_code = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)
    branch_id = models.CharField(max_length=255)
    lon_sys_id = models.CharField(max_length=255, blank=True, null=True)
    loan_id = models.CharField(max_length=255)
    lon_open_date = models.DateTimeField(blank=True, null=True)
    lon_exp_date = models.DateTimeField(blank=True, null=True)
    lon_ext_date = models.DateTimeField(blank=True, null=True)
    lon_int_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lon_purpose_code = models.CharField(max_length=255, blank=True, null=True)
    lon_credit_line = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    lon_currency_code = models.CharField(max_length=10, blank=True, null=True)
    lon_outstanding_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    lon_account_no = models.CharField(max_length=255, blank=True, null=True)
    lon_no_days_slow = models.IntegerField(blank=True, null=True)
    lon_class = models.CharField(max_length=255, blank=True, null=True)
    lon_type = models.CharField(max_length=255, blank=True, null=True)
    lon_term = models.CharField(max_length=255, blank=True, null=True)
    lon_status = models.CharField(max_length=255, blank=True, null=True)
    lon_insert_date = models.DateTimeField(blank=True, null=True)
    lon_update_date = models.DateTimeField(blank=True, null=True)
    lon_applied_date = models.DateTimeField(blank=True, null=True)
    is_disputed = models.BigIntegerField(default=0, null=True)
    def save(self, *args, **kwargs):
        self.lon_no_days_slow = self.lon_no_days_slow or 0
        self.is_disputed = self.is_disputed or 0
        
        if not isinstance(self.lon_no_days_slow, int):
            raise ValidationError("lon_no_days_slow must be an integer")
        if not isinstance(self.is_disputed, int):
            raise ValidationError("is_disputed must be an integer")
            
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('bnk_code', 'branch_id', 'customer_id', 'loan_id')
class B1_Daily(models.Model):
    lcicID = models.CharField(max_length=25,null=True)
    daily = models.DateField(blank=True)
    period = models.CharField(max_length=150)
    com_enterprise_code = models.CharField(max_length=25)
    segmentType = models.CharField(max_length=10)
    bnk_code = models.CharField(max_length=10)
    customer_id = models.CharField(max_length=30)
    branch_id = models.CharField(max_length=30)
    lon_sys_id = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    lon_open_date = models.DateField(blank=True)
    lon_exp_date = models.DateField(blank=True)
    lon_ext_date = models.DateField(blank=True, null=True)
    lon_int_rate = models.FloatField(default=0, null=True)
    lon_purpose_code = models.CharField(max_length=30)
    lon_credit_line = models.BigIntegerField(default=0, null=True)
    lon_currency_code = models.CharField(max_length=10)
    lon_outstanding_balance = models.BigIntegerField(default=0,null=True)
    lon_account_no = models.CharField(max_length=30)
    lon_no_days_slow = models.CharField(max_length=30)
    lon_class = models.CharField(max_length=10)
    lon_type = models.CharField(max_length=10)
    lon_term = models.CharField(max_length=25)
    lon_status = models.CharField(max_length=10)
    lon_insert_date = models.DateTimeField(blank=True)
    lon_update_date = models.DateTimeField(blank=True)
    lon_applied_date = models.DateTimeField(blank=True)
    is_disputed = models.BigIntegerField(default=0, null=True)
 


    
class B1_Yearly(models.Model):
    lcicID = models.CharField(max_length=25,null=True)
    period = models.CharField(max_length=150)
    com_enterprise_code = models.CharField(max_length=25)
    segmentType = models.CharField(max_length=10)
    bnk_code = models.CharField(max_length=10)
    customer_id = models.CharField(max_length=30)
    branch_id = models.CharField(max_length=30)
    lon_sys_id = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    lon_open_date = models.DateField(blank=True)
    lon_exp_date = models.DateField(blank=True)
    lon_ext_date = models.DateField(blank=True, null=True)
    lon_int_rate = models.FloatField(default=0, null=True)
    lon_purpose_code = models.CharField(max_length=30)
    lon_credit_line = models.BigIntegerField(default=0, null=True)
    lon_currency_code = models.CharField(max_length=10)
    lon_outstanding_balance = models.BigIntegerField(default=0,null=True)
    lon_account_no = models.CharField(max_length=30)
    lon_no_days_slow = models.CharField(max_length=30)
    lon_class = models.CharField(max_length=10)
    lon_type = models.CharField(max_length=10)
    lon_term = models.CharField(max_length=25)
    lon_status = models.CharField(max_length=10)
    lon_insert_date = models.DateTimeField(blank=True)
    lon_update_date = models.DateTimeField(blank=True)
    lon_applied_date = models.DateTimeField(blank=True)
    is_disputed = models.BigIntegerField(default=0, null=True)
    
# class EnterpriseInfo(models.Model):
#     LCICID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     EnterpriseID = models.CharField(max_length=50,blank=True,null=True)
#     enterpriseNameLao = models.CharField(max_length=255,blank=True,null=True)
#     eneterpriseNameEnglish = models.CharField(max_length=255,blank=True,null=True)
#     regisCertificateNumber = models.CharField(max_length=50,blank=True,null=True)
#     regisDate = models.DateTimeField(blank=True, null=True)
#     enLocation = models.CharField(max_length=50,blank=True,null=True)
#     regisStrationOfficeType = models.CharField(max_length=50,blank=True,null=True)
#     regisStationOfficeCode = models.CharField(max_length=50,blank=True,null=True)
#     enLegalStrature = models.CharField(max_length=500,blank=True,null=True)
#     foreigninvestorFlag = models.CharField(max_length=500,blank=True,null=True)
#     investmentAmount = models.FloatField(null=True, blank=True)
#     investmentCurrency = models.CharField(max_length=50,blank=True,null=True)
#     representativeNationality = models.CharField(max_length=50,blank=True,null=True)
#     LastUpdate = models.DateTimeField(blank=True,null=True)
#     CancellationDate = models.DateTimeField(blank=True,null=True)
#     InsertDate = models.DateTimeField(blank=True, null=True,auto_now_add=True)
#     UpdateDate = models.DateTimeField(blank=True, null=True)

# lcicHome/models.py

from django.db import models

class EnterpriseInfo(models.Model):
    LCICID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    EnterpriseID = models.CharField(max_length=50, blank=True, null=True)
    enterpriseNameLao = models.CharField(max_length=255, blank=True, null=True)
    eneterpriseNameEnglish = models.CharField(max_length=255, blank=True, null=True)
    regisCertificateNumber = models.CharField(max_length=50, blank=True, null=True)
    regisDate = models.DateTimeField(blank=True, null=True)
    enLocation = models.CharField(max_length=50, blank=True, null=True)
    regisStrationOfficeType = models.CharField(max_length=50, blank=True, null=True)
    regisStationOfficeCode = models.CharField(max_length=50, blank=True, null=True)
    enLegalStrature = models.CharField(max_length=500, blank=True, null=True)
    foreigninvestorFlag = models.CharField(max_length=500, blank=True, null=True)
    investmentAmount = models.FloatField(null=True, blank=True)
    investmentCurrency = models.CharField(max_length=50, blank=True, null=True)
    representativeNationality = models.CharField(max_length=50, blank=True, null=True)
    LastUpdate = models.DateTimeField(blank=True, null=True)
    CancellationDate = models.DateTimeField(blank=True, null=True)
    InsertDate = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    UpdateDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"EnterpriseInfo {self.LCICID} - {self.enterpriseNameLao}"


class InvestorInfo(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    EnterpriseID = models.CharField(max_length=50,blank=True,null=True)
    investorName = models.CharField(max_length=255,blank=True,null=True)
    investorOwnerPercentage = models.CharField(max_length=100,blank=True,null=True)
    investorNationality = models.CharField(max_length=50,blank=True,null=True)
    investorcardNumber = models.CharField(max_length=100,blank=True,null=True)
    investorMobile = models.CharField(max_length=50,blank=True,null=True)
    InsertDate = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    UpdateDate = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return f"InvestorInfo {self.ID} - {self.investorName}"
    
    
    
class ISISCode(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    EnterpriseID = models.CharField(max_length=50,blank=True,null=True)
    IsisCodes = models.CharField(max_length=255,blank=True,null=True)
    IsisName = models.CharField(max_length=4000,blank=True,null=True)
    InsertDate = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    UpdateDate = models.DateTimeField(blank=True,null=True)
    
class user_logged(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    user = models.ForeignKey(Login, on_delete = models.CASCADE)
    ip_address = models.GenericIPAddressField()
    login_time = models.DateTimeField(auto_now_add=True)

class Rp_type(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    Rp_NameL = models.CharField(max_length=255, blank=True, null=True)
    Rp_NameE = models.CharField(max_length=255, blank=True, null=True)

class searchLog(models.Model):
    search_ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    enterprise_ID = models.CharField(max_length=50,blank=True,null=True)
    LCIC_ID = models.CharField(max_length=50,blank=True,null=True)
    bnk_code = models.CharField(max_length=255, blank=True, null=True)
    cus_ID = models.CharField(max_length=255, blank=True, null=True)
    credit_type = models.CharField(max_length=255, blank=True, null=True)
    inquiry_date = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    inquiry_month = models.DateField(blank=True,null=True)
    inquiry_time = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    com_tel = models.CharField(max_length=255, blank=True, null=True)
    com_location = models.CharField(max_length=255, blank=True, null=True)
    rec_loan_amount = models.FloatField(default=0, null=True)
    rec_loan_amount_currency = models.CharField(max_length=255, blank=True, null=True)
    rec_loan_purpose = models.CharField(max_length=255, blank=True, null=True)
    rec_enquiry_type = models.CharField(max_length=255, blank=True, null=True)
    cusType = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
 
class request_charge(models.Model):
    rec_charge_ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    bnk_code = models.CharField(max_length=255, blank=True, null=True)
    chg_amount = models.FloatField(max_length=255, blank=True,null=True)
    chg_code = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    insert_date = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    rtp_code = models.CharField(max_length=255, blank=True, null=True)
    chg_unit = models.CharField(max_length=255, blank=True, null=True)
    user_sys_id = models.CharField(max_length=255, blank=True, null=True)
    LCIC_ID = models.CharField(max_length=255, blank=True, null=True)
    cusType = models.CharField(max_length=255, blank=True, null=True)
    user_session_id = models.CharField(max_length=255, blank=True, null=True)
    rec_reference_code = models.CharField(max_length=255, blank=True, null=True)
    rec_insert_date = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    
       

from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    size = models.FloatField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models

class UploadedJSONFile(models.Model):
    file_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=500)

    def __str__(self):
        return self.file_name



from django.db import models


class File(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploadFiles/')

    def __str__(self):
        return self.title

class CustomLoginToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(Login, related_name='auth_token', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def refresh(self):
        self.key = binascii.hexlify(os.urandom(20)).decode()
        self.expires_at = timezone.now() + timedelta(minutes=5)
        self.save()

    def __str__(self):
        return self.key

class Role(models.Model):
    name = models.CharField(max_length=100)
    can_access_all_paths = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class SidebarItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role, related_name="sidebar_items")

class SidebarSubItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey(SidebarItem, on_delete=models.CASCADE, related_name="sub_items")
    roles = models.ManyToManyField(Role, related_name="sidebar_sub_items")

class Path(models.Model):
    path_name = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role, related_name='accessible_paths')

    def __str__(self):
        return self.path_name

# Khor Colleteral

class C1 (models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    bnk_code = models.CharField(max_length=30)
    period = models.CharField(max_length=150)
    segmentType = models.CharField(max_length=10)
    branch_id_code = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=50)
    loan_id = models.CharField(max_length=50)
    col_id = models.CharField(max_length=30) 
    col_type = models.CharField(max_length=30)
    collateral_status = models.CharField(max_length=30)
    insert_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)
    lcicID = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    com_enterprise_code = models.CharField(max_length=50)
class C1_disptes (models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    bnk_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    branch_id_code = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=50)
    loan_id = models.CharField(max_length=50)
    col_id = models.CharField(max_length=30) 
    col_type = models.CharField(max_length=30)
    collateral_status = models.CharField(max_length=30)
    insert_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)
    lcicID = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    com_enterprise_code = models.CharField(max_length=50)

from django.db import models
from django.utils import timezone

class C_error(models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    branch_id_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    bnk_code = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=50)
    loan_id = models.CharField(max_length=50)
    col_id = models.CharField(max_length=30) 
    col_type = models.CharField(max_length=30)
    datamatch = models.CharField(max_length=30)  
    collateral_status = models.CharField(max_length=30)
    collateral_insert_date = models.DateTimeField(blank=True)
    collateral_update_date = models.DateTimeField(blank=True)
    lcicID = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    com_enterprise_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.lcicID} - {self.com_enterprise_code} - {self.collateral_status}"

    


class col_real_estates(models.Model):
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    lcicID = models.CharField(max_length=30)
    bnk_code = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=50)
    segmentType = models.CharField(max_length=10)
    branch_id_code = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    col_type = models.CharField(max_length=30)
    value_unit = models.CharField(max_length=30)
    com_enterprise_code = models.CharField(max_length=255)
    plot_vilid = models.CharField(max_length=30)  # ລະຫັດບ້ານທີ່ຕັ້ງຂອງດິນ
    plot_unit = models.CharField(max_length=30)  # ໜວ່ຍ
    col_id = models.CharField(max_length=30)  # ລະຫັດຫຼັກຊັບ 
    col_value = models.CharField(max_length=50)  # ລາຄາ
    land_no = models.CharField(max_length=30)  # ເລກທີດິນ
    place_regist_land = models.CharField(max_length=30)  
    land_map_no = models.CharField(max_length=30)  
    land_out_time = models.CharField(max_length=30)  # ອອກຄັ້ງທີ
    col_area = models.CharField(max_length=30)  # ເຂດ
    land_registry_book_no = models.CharField(max_length=30)  # ປື້ມທະບຽນທີ່ດີນເຫຼັ້ມທີ່
    land_plot_no = models.CharField(max_length=30)  # ຕອນດີນເລກທີ່
    land_document_no = models.CharField(max_length=30)  # ໃບທີ່ດີນເລກທີ່
    land_out_time = models.CharField(max_length=30)  # ອອກຄັ້ງທີ່ດີນເລກທີ່
    land_area = models.DecimalField(max_digits=10, decimal_places=2)  # ເນື້ອທີ
    land_regis_date = models.CharField()  # ວັນທີອອກໃບຕທດິນ
    land_type = models.CharField(max_length=30)  # ປະເພດດິນ
    land_unit = models.CharField(max_length=30)  # ມາດຕາສວນ
    place_regist_no = models.CharField(max_length=30)  # ສະຖານທີ່ອອກໃບຕາດິນ
    owner_name = models.CharField(max_length=100)  # ອອກໃຫ້ແກ່
    owner_birth_date = models.CharField()  # ວັນ.ເດືອນ.ປີເກີດ
    owner_gender = models.CharField(max_length=30)
    owner_nationality = models.CharField(max_length=30)  # ສັນຊາດ
    owner_occupation = models.CharField(max_length=50)  # ອາຊີບ
    current_unit = models.CharField(max_length=30)  # ໜວ່ຍ ປະຈຸບັນ
    current_vilid = models.CharField(max_length=30)  # ລະຫັດບ້ານ ປະຈຸບັນ
    spouse_name = models.CharField(max_length=100, blank=True, null=True)  # ຊື່ຜົວ ຫຼື ເມຍ
    spouse_birth_date = models.CharField(blank=True, null=True)  # ວັນ.ເດືອນ.ປີເກີດ (ຊື່ຜົວ ຫຼື ເມຍ)
    spouse_nationality = models.CharField(max_length=30, blank=True, null=True)  # ສັນຊາດ (ຊື່ຜົວ ຫຼື ເມຍ)
    spouse_occupation = models.CharField(max_length=50, blank=True, null=True)  # ອາຊີບ (ຊື່ຜົວ ຫຼື ເມຍ)
    land_acquisition = models.CharField(max_length=100)  # ການໄດ້ມາຂອງສິດນຳໃຊ້ດິນ
    ownership_status = models.CharField(max_length=50)  # ສະຖານະເປັນເຈົ້າຂອງ
    user_id = models.CharField(max_length=100)
    rel_status = models.CharField(max_length=100)
    owner_name_lao = models.CharField(max_length=100)
    owner_surname_lao = models.CharField(max_length=100)
    insert_date = models.DateField()
    update_date = models.DateField()

    class Meta:
        db_table = "col_real_estate"


class col_money_mia (models.Model):  #ເອກະສານມີຄ່າ C2.2
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    lcicID = models.CharField(max_length=30)
    bnk_code = models.CharField(max_length=30)
    com_enterprise_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    # col_id = models.CharField(max_length=30)
    col_type = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=30)
    branch_id_code = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    col_id = models.CharField(max_length=30)
    account_no = models.CharField(max_length=30)
    account_type = models.CharField(max_length=30)
    value_unit = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    owner_gender = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    owner_surname = models.CharField(max_length=30)
    owner_lao_name = models.CharField(max_length=30)
    owner_lao_surname = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    insert_date = models.DateField()
    update_date = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.com_enterprise_code}"

    class Meta:
        db_table = "col_money_mia"

class col_equipment_eqi (models.Model):  # ເຄື່ອງຈັກ ແລະ ອຸປະກອນຕ່າງໆ C2.3
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    bank_customer_ID = models.CharField(max_length=30)
    bnk_code = models.CharField(max_length=30)
    lcicID = models.CharField(max_length=30)
    com_enterprise_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    col_type = models.CharField(max_length=30)
    branch_id_code = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    col_id = models.CharField(max_length=30)
    machine_type = models.CharField(max_length=30)
    machine_no = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    machine_status = models.CharField(max_length=30)
    value_unit = models.CharField(max_length=30)
    owner_gender = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    owner_surname = models.CharField(max_length=30)
    owner_lao_name = models.CharField(max_length=30)
    owner_lao_surname = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    insert_date = models.DateField()
    update_date = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.com_enterprise_code}"

    class Meta:
        db_table = "col_equipment_eqi"

class col_project_prj (models.Model):  # ເຄື່ອງຈັກ ແລະ ອຸປະກອນຕ່າງໆ C2.4
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    bank_customer_ID = models.CharField(max_length=30)
    bnk_code = models.CharField(max_length=30)
    lcicID = models.CharField(max_length=30)
    com_enterprise_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    col_type = models.CharField(max_length=30)
    branch_id_code = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    project_type = models.CharField(max_length=30)
    col_id = models.CharField(max_length=30)
    project_name_en = models.CharField(max_length=30)
    ministry = models.CharField(max_length=30)
    project_number = models.CharField(max_length=30)
    project_status = models.CharField(max_length=30)
    value_unit = models.CharField(max_length=30)
    owner_gender = models.CharField(max_length=30)
    project_name_la = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    owner_surname = models.CharField(max_length=30)
    owner_lao_name = models.CharField(max_length=30)
    owner_lao_surname = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    insert_date = models.DateField()
    update_date = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.com_enterprise_code}"

    class Meta:
        db_table = "col_project_prj"
class col_vechicle_veh (models.Model):  # ຂໍ້ມູນຍານພາຫະນະ C2.5
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    lcicID = models.CharField(max_length=30)
    bnk_code = models.CharField(max_length=30)
    com_enterprise_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    col_type = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=30)
    branch_id_code = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    col_id = models.CharField(max_length=30)
    name_owner = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=30)
    engine_number = models.CharField(max_length=30)
    body_number = models.CharField(max_length=30)
    value_unit = models.CharField(max_length=30)
    # vehicle_value_unit = models.CharField(max_length=30)
    vehicle_status = models.CharField(max_length=30)
    owner_gender = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    owner_surname = models.CharField(max_length=30)
    owner_lao_name = models.CharField(max_length=30)
    owner_lao_surname = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    insert_date = models.DateField()
    update_date = models.DateField()
    

    def __str__(self):
        return f"{self.id} - {self.com_enterprise_code}"

    class Meta:
        db_table = "col_vechicle_veh"

class col_guarantor_gua (models.Model):  # ຂໍ້ມູນຜູ້ຄໍ້າ C2.6 1
    id = models.AutoField(primary_key=True) #1
    id_file = models.CharField(max_length=100) 
    period = models.CharField(max_length=150)
    lcicID = models.CharField(max_length=30)
    bnk_code = models.CharField(max_length=30)
    com_enterprise_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    col_type = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=30)
    branch_id_code = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    col_id = models.CharField(max_length=30)
    guarantor_type = models.CharField(max_length=30)
    guarantor_nationality = models.CharField(max_length=30)
    national_id = models.CharField(max_length=30)
    national_expiry_date = models.CharField(max_length=30)
    passport = models.CharField(max_length=30)
    passport_expiry_date = models.CharField(max_length=30)
    familybook = models.CharField(max_length=30)
    familybook_province_code_of_issue = models.CharField(max_length=30)
    familybook_issue_date = models.CharField(max_length=30)
    birthdate = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    ist_name_english = models.CharField(max_length=30)
    ist_name_lao = models.CharField(max_length=30)
    nickname_english = models.CharField(max_length=30)
    nickname_lao = models.CharField(max_length=30)
    surname_english = models.CharField(max_length=30)
    surname_lao = models.CharField(max_length=30)
    address_number_street_english = models.CharField(max_length=30)
    address_number_street_lao = models.CharField(max_length=30)
    address_village_english = models.CharField(max_length=30)
    address_village_lao = models.CharField(max_length=30)
    address_sub_district_english = models.CharField(max_length=30)
    address_sub_district_lao = models.CharField(max_length=30)
    value_unit = models.CharField(max_length=30)
    address_district_english = models.CharField(max_length=30)
    address_district_lao = models.CharField(max_length=30)
    address_province_code = models.CharField(max_length=30)
    owner_gender = models.CharField(max_length=30)
    enterprise_code = models.CharField(max_length=30)
    registration_date_of_issue = models.CharField(max_length=30)
    registration_place_issue = models.CharField(max_length=30)
    company_name_english = models.CharField(max_length=30)
    company_name_lao = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    insert_date = models.DateField()
    update_date = models.DateField()
    def __str__(self):
        return f"{self.id} - {self.com_enterprise_code}"

    class Meta:
        db_table = "col_guarantor_gua"

class col_goldsilver_gold (models.Model):  # ເງິນ ແລະ ຄຳ C2.7
    id = models.AutoField(primary_key=True)
    id_file = models.CharField(max_length=100)
    period = models.CharField(max_length=150)
    lcicID = models.CharField(max_length=30)
    bnk_code = models.CharField(max_length=30)
    segmentType = models.CharField(max_length=10)
    com_enterprise_code = models.CharField(max_length=30)
    col_type = models.CharField(max_length=30)
    bank_customer_ID = models.CharField(max_length=30)
    branch_id_code = models.CharField(max_length=30)
    loan_id = models.CharField(max_length=30)
    col_id = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    gld_status = models.CharField(max_length=30)
    owner_gender = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    owner_surname = models.CharField(max_length=30)
    value_unit = models.CharField(max_length=30)
    owner_lao_name = models.CharField(max_length=30)
    owner_lao_surname = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    user_id = models.CharField(max_length=100)
    insert_date = models.DateField()
    update_date = models.DateField()
    def __str__(self):
        return f"{self.id} - {self.com_enterprise_code}"

    class Meta:
        db_table = "col_goldsilver_gold"