# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class JsonfileWater(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    upload_date = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Jsonfile_water'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Test(models.Model):
    name_lcic = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'test'
        
class FileDetail(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.FileField(upload_to="json_uploads/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    processed_items = models.IntegerField(default=0)  # New field to track progress

    class Meta:
        db_table = "file_detail"

class UploadJsonFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    upload_date = models.DateTimeField()
    # user_upload = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    
    class Meta:
        managed = False
        db_table = 'file_detail'
        

class Utility_Bill(models.Model):
    BillID = models.AutoField(primary_key=True)
    Customer_ID = models.CharField(max_length=255)
    InvoiceNo = models.CharField(max_length=255)
    TypeOfPro = models.CharField(max_length=100)
    Outstanding = models.DecimalField(max_digits=100, decimal_places=2)
    Basic_Tax = models.DecimalField(max_digits=100, decimal_places=2)
    Bill_Amount = models.DecimalField(max_digits=100, decimal_places=2)
    Debt_Amount = models.DecimalField(max_digits=100, decimal_places=2)
    Payment_ID = models.TextField()
    PaymentType = models.TextField()
    Payment_Date = models.TextField()
    InvoiceMonth = models.CharField(max_length=50)
    InvoiceDate = models.CharField(max_length=100)
    DisID = models.CharField(max_length=100)
    ProID = models.CharField(max_length=100)
    InsertDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    UserID = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f"Bill {self.BillID} - {self.Customer_ID}"
    
    
      
class File_Electric(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.FileField(upload_to="electric_json_uploads/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    processed_items = models.IntegerField(default=0)  # New field to track progress

    class Meta:
        db_table = "file_electric"
        
class Electric_Bill(models.Model):
    BillID = models.AutoField(primary_key=True)
    Customer_ID = models.CharField(max_length=255)
    InvoiceNo = models.CharField(max_length=255)
    TypeOfPro = models.CharField(max_length=100)
    Outstanding = models.DecimalField(max_digits=100, decimal_places=2)
    Basic_Tax = models.DecimalField(max_digits=100, decimal_places=2)
    Bill_Amount = models.DecimalField(max_digits=100, decimal_places=2)
    Debt_Amount = models.DecimalField(max_digits=100, decimal_places=2)
    Payment_ID = models.TextField()
    PaymentType = models.TextField()
    Payment_Date = models.TextField()
    InvoiceMonth = models.CharField(max_length=50)
    InvoiceDate = models.CharField(max_length=100)
    DisID = models.CharField(max_length=100)
    ProID = models.CharField(max_length=100)
    InsertDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    UserID = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f"Bill {self.BillID} - {self.Customer_ID}"

class UtilityBillUpload(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
class w_customer_info(models.Model):
    No =  models.CharField(max_length=100)
    Customer_ID = models.CharField(max_length=100)
    Company_name = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    National_ID = models.CharField(max_length=100)
    Passport = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Dustrict_ID = models.CharField(max_length=100)
    Province_ID = models.CharField(max_length=100)
    Tel = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Cus_type = models.CharField(max_length=100)
    Regis_date = models.CharField(max_length=100)
   
     
class edl_customer_info(models.Model):
    No =  models.CharField(max_length=100)
    Customer_ID = models.CharField(max_length=100)
    Company_name = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    National_ID = models.CharField(max_length=100)
    Passport = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Dustrict_ID = models.CharField(max_length=100)
    Province_ID = models.CharField(max_length=100)
    Tel = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Cus_type = models.CharField(max_length=100)
    Regis_date = models.CharField(max_length=100)
   
   
class searchlog_utility(models.Model):
    search_id = models.BigAutoField(auto_created=True, primary_key=True)
    bnk_code = models.CharField(max_length=100)
    sys_usr = models.CharField(max_length=100)
    edl_cusid = models.CharField(max_length=100, blank=True, default='')
    wt_cusid = models.CharField(max_length=100, blank=True, default='')
    tel_cusid = models.CharField(max_length=100, blank=True, default='')
    proID_edl = models.CharField(max_length=100, blank=True, default='')
    proID_wt = models.CharField(max_length=100, blank=True, default='')
    proID_tel = models.CharField(max_length=100, blank=True, default='')
    credittype = models.CharField(max_length=100)
    inquiry_date = models.DateTimeField(auto_now_add=True)  # Changed to DateTimeField
    inquiry_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search {self.search_id} - {self.sys_usr}"

class request_charge_utility(models.Model):
    rec_sys_id = models.BigAutoField(auto_created=True, primary_key=True)
    usr_session_id = models.CharField(max_length=100)
    search_id = models.ForeignKey(searchlog_utility, on_delete=models.CASCADE)
    bnk_code = models.CharField(max_length=100)
    chg_code = models.CharField(max_length=100)
    chg_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField
    chg_unit = models.CharField(max_length=100)
    sys_usr = models.CharField(max_length=100)
    credit_type = models.CharField(max_length=100)
    edl_cusid = models.CharField(max_length=100, blank=True, default='')
    wt_cusid = models.CharField(max_length=100, blank=True, default='')
    tel_cusid = models.CharField(max_length=100, blank=True, default='')
    proID_edl = models.CharField(max_length=100, blank=True, default='')
    proID_wt = models.CharField(max_length=100, blank=True, default='')
    proID_tel = models.CharField(max_length=100, blank=True, default='')
    rec_reference_code = models.CharField(max_length=255)
    rec_insert_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Charge {self.rec_sys_id} - {self.sys_usr}"
    
class edl_province_code(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    pro_id = models.CharField(max_length=50)
    pro_name = models.CharField(max_length=100)
    
class edl_district_code(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    pro_id = models.CharField(max_length=50)
    dis_id = models.CharField(max_length=50)
    dis_name = models.CharField(max_length=100)
