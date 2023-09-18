from sre_parse import Verbose
from tabnanny import verbose
from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.html import format_html
from lcicNews.models import*
from .validators import validate_file_extension


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
    def __str__(self):
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
    def __str__(seft):
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
    def __str__(self):
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
    def __str__(seft):
        return seft.nameL

class H_userInfo(models.Model):
    code = models.CharField(max_length=50)
    nameL = models.CharField(max_length=100)
    nameE = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='userInfo'
    def __str__(seft):
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
    nFiles = models.FileField(upload_to='uploadNewsFlils',null=True,blank=True)
    published = models.BooleanField(default=False)
    insertDate = models.DateTimeField(auto_now_add = True)
    updateDate = models.DateTimeField(auto_now = True)
    class Meta:
        ordering =['-id']
        verbose_name_plural='newsInfo'
    def __str__(self):
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
    def __str__(self):
        return self.commandL
    
class H_Lang(models.Model):
    id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Trans_LA = models.TextField(null=True,blank=True)
    Trans_EN = models.TextField(null=True,blank=True)
    
    
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
    def __str__(self):
        return self.nameL
    
    
class Menu(models.Model):
    MID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameL = models.CharField(max_length=150)
    nameE = models.CharField(max_length=150)
    class Meta:
        # ordering=('MID')
        verbose_name_plural='Nav_Menu'
    def __str__(self):
        return self.nameL

class SubMenu(models.Model):
    SMID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    MID = models.ForeignKey(Menu,  null=True, blank=True ,on_delete=models.CASCADE)
    nameL = models.CharField(max_length=150)
    nameE = models.CharField(max_length=150)
    class Meta:
        # ordering='SMID'
        verbose_name_plural='Nav_Submenu'
    def __str__(self):
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

class Login(models.Model):
    UID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    MID = models.ForeignKey(memberInfo, related_name='memberInfo', null=True, blank=True, on_delete=models.CASCADE)
    GID = models.ForeignKey(User_Group, null=True, blank=True , on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    nameL = models.CharField(max_length=150)
    nameE = models.CharField(max_length=150)
    surnameL = models.CharField(max_length=150)
    surnameE = models.CharField(max_length=150)
    insertDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updateDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    is_active = models.BooleanField(default=True)
    
    
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
    def __str__(seft):
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
    def __str__(self):
        return self.SType
    
    
class SType(models.Model):
    SType = models.CharField(max_length=150, null=False)
    nameL = models.CharField(max_length=150, null=False, blank=True)
    nameE = models.CharField(max_length=150, null=False, blank=True)
    class meta:
        ordering=['SType']
        verbose_name_plural ='SegmentType'
    def __str__(self):
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
    def __str__(self):
        return self.nameL

class Upload_File(models.Model):
    FID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
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
    
class B1(models.Model):
    lcicID = models.CharField(max_length=25,null=True)
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
    
    
class B1_Monthly(models.Model):
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
    
class EnterpriseInfo(models.Model):
    LCICID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    EnterpriseID = models.CharField(max_length=50,blank=True,null=True)
    enterpriseNameLao = models.CharField(max_length=255,blank=True,null=True)
    eneterpriseNameEnglish = models.CharField(max_length=255,blank=True,null=True)
    regisCertificateNumber = models.CharField(max_length=50,blank=True,null=True)
    regisDate = models.DateTimeField(blank=True, null=True)
    enLocation = models.CharField(max_length=50,blank=True,null=True)
    regisStrationOfficeType = models.CharField(max_length=50,blank=True,null=True)
    regisStationOfficeCode = models.CharField(max_length=50,blank=True,null=True)
    enLegalStrature = models.CharField(max_length=500,blank=True,null=True)
    foreigninvestorFlag = models.CharField(max_length=500,blank=True,null=True)
    investmentAmount = models.FloatField(null=True, blank=True)
    investmentCurrency = models.CharField(max_length=50,blank=True,null=True)
    representativeNationality = models.CharField(max_length=50,blank=True,null=True)
    LastUpdate = models.DateTimeField(blank=True,null=True)
    CancellationDate = models.DateTimeField(blank=True,null=True)
    InsertDate = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    UpdateDate = models.DateTimeField(blank=True, null=True)
    
    
    
class InvestorInfo(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    EnterpriseID = models.CharField(max_length=50,blank=True,null=True)
    IsisCodes = models.CharField(max_length=255,blank=True,null=True)
    IsisName = models.CharField(max_length=255,blank=True,null=True)
    InsertDate = models.DateTimeField(blank=True,null=True)
    UpdateDate = models.DateTimeField(blank=True,null=True)
    
class ISISCode(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    EnterpriseID = models.CharField(max_length=50,blank=True,null=True)
    investorName = models.CharField(max_length=255,blank=True,null=True)
    investorOwnerPercentage = models.CharField(max_length=100,blank=True,null=True)
    investorNationality = models.CharField(max_length=50,blank=True,null=True)
    investorcardNumber = models.CharField(max_length=100,blank=True,null=True)
    investorMobile = models.CharField(max_length=50,blank=True,null=True)
    InsertDate = models.DateTimeField(blank=True,null=True)
    UpdateDate = models.DateTimeField(blank=True,null=True)
    