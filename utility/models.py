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
    InsertDate = models.CharField(max_length=150, null=True, blank=True)
    UpdateDate = models.CharField(max_length=150, null=True, blank=True)
    class Meta:
        indexes = [
            models.Index(fields=['Name', 'Province_ID'], name='water_name_prov_idx'),
            models.Index(fields=['Surname', 'Province_ID'], name='water_surname_prov_idx'),
        ]
    
    def __str__(self):
        return f"{self.Customer_ID} - {self.Name} {self.Surname or ''}"
    
     
# class edl_customer_info(models.Model):
#     No =  models.CharField(max_length=100)
#     Customer_ID = models.CharField(max_length=100)
#     Company_name = models.CharField(max_length=100)
#     Name = models.CharField(max_length=100)
#     Surname = models.CharField(max_length=100)
#     National_ID = models.CharField(max_length=100)
#     Passport = models.CharField(max_length=100)
#     Address = models.CharField(max_length=100)
#     Dustrict_ID = models.CharField(max_length=100)
#     Province_ID = models.CharField(max_length=100)
#     Tel = models.CharField(max_length=100)
#     Email = models.CharField(max_length=100)
#     Cus_type = models.CharField(max_length=100)
#     Regis_date = models.CharField(max_length=100)
class edl_customer_info(models.Model):
    No = models.CharField(max_length=100)
    Customer_ID = models.CharField(max_length=100, db_index=True)  # Add index
    Company_name = models.CharField(max_length=500, db_index=True)  # Add index
    Name = models.CharField(max_length=500, db_index=True)  # Add index
    Surname = models.CharField(max_length=500, db_index=True)  # Add index
    National_ID = models.CharField(max_length=100)
    Passport = models.CharField(max_length=100)
    Address = models.TextField()
    Dustrict_ID = models.CharField(max_length=100, db_index=True)  # Add index
    Province_ID = models.CharField(max_length=100, db_index=True)  # Add index
    Tel = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Cus_type = models.CharField(max_length=100)
    Regis_date = models.CharField(max_length=100)
    InsertDate = models.CharField(max_length=50, null=True, blank=True)
    UpdateDate = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        # Composite indexes for faster searches
        indexes = [
            models.Index(fields=['Name', 'Province_ID'], name='name_province_idx'),
            models.Index(fields=['Surname', 'Province_ID'], name='surname_province_idx'),
            models.Index(fields=['Company_name', 'Province_ID'], name='company_province_idx'),
        ]
    
    def __str__(self):
        return f"{self.Customer_ID} - {self.Name} {self.Surname}"
   
   
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

    
class w_province_code(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    pro_id = models.CharField(max_length=50)
    pro_name = models.CharField(max_length=100)
    
    
class w_district_code(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    pro_id = models.CharField(max_length=50)
    dis_id = models.CharField(max_length=50)
    dis_name = models.CharField(max_length=100)

# API Edl Tracking:
from django.utils import timezone
# pherm check update
class UploadDataTracking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('partial', 'Partial')
    ]
    
    pro_id = models.CharField(max_length=10, db_index=True)
    pro_name = models.CharField(max_length=100)
    dis_id = models.CharField(max_length=10, db_index=True)
    dis_name = models.CharField(max_length=100)
    upload_month = models.CharField(max_length=6, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_records = models.IntegerField(default=0)
    data_size_mb = models.FloatField(default=0.0)
    upload_started = models.DateTimeField(null=True, blank=True)
    upload_completed = models.DateTimeField(null=True, blank=True)
    payment_records = models.IntegerField(default=0)  # ✅ ADD THIS
    customer_records = models.IntegerField(default=0)  # ✅ ADD THIS
    upload_duration = models.FloatField(null=True, blank=True)  # ✅ ADD THIS (optional)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    processed_records = models.IntegerField(default=0)
    failed_records = models.IntegerField(default=0)
    user_upload = models.CharField(max_length=50, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    api_response_code = models.IntegerField(null=True, blank=True)
    success_rates = models.FloatField(default=0.0, blank=True, null=True)  # New field for success rate percentage
    
    class Meta:
        unique_together = ['pro_id', 'dis_id', 'upload_month']
        indexes = [
            models.Index(fields=['upload_month', 'status']),
            models.Index(fields=['pro_id', 'dis_id']),
        ]
    
    def __str__(self):
        return f"{self.pro_name} - {self.dis_name} ({self.upload_month}) - {self.status}"
    
    @property
    def upload_duration(self):
        if self.upload_started and self.upload_completed:
            return (self.upload_completed - self.upload_started).total_seconds()
        return None
    
    @property
    def is_uploaded_this_month(self):
        current_month = timezone.now().strftime('%Y%m')
        return self.upload_month == current_month and self.status == 'completed'
    

class UploadLog(models.Model):
    tracking = models.ForeignKey(UploadDataTracking, on_delete=models.CASCADE, related_name='logs')
    log_level = models.CharField(max_length=10, choices=[
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error')
    ])
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        
        
# Water Supply Data Load Tracking --------------------------------------------------

from django.db import models
from django.utils import timezone

class WaterUploadDataTracking(models.Model):
    """
    Tracking model for water supply data uploads
    Matches electric supply structure with separate payment and customer records
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('partial', 'Partial')
    ]
    
    # Location Information
    pro_id = models.CharField(max_length=10, db_index=True)
    pro_name = models.CharField(max_length=100)
    dis_id = models.CharField(max_length=10, db_index=True)
    dis_name = models.CharField(max_length=100)
    
    # Period and Status
    upload_month = models.CharField(max_length=6, db_index=True)  # Format: YYYYMM
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Record Counts (UPDATED: Separate payment and customer records)
    total_records = models.IntegerField(default=0)  # Total bills/payments
    payment_records = models.IntegerField(default=0)  # Payment records inserted
    customer_records = models.IntegerField(default=0)  # Customer records inserted
    
    # Processing Information
    data_size_mb = models.FloatField(default=0.0)
    upload_started = models.DateTimeField(null=True, blank=True)
    upload_completed = models.DateTimeField(null=True, blank=True)
    upload_duration = models.FloatField(null=True, blank=True)  # Duration in seconds
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Statistics
    processed_records = models.IntegerField(default=0)
    failed_records = models.IntegerField(default=0)
    success_rates = models.FloatField(default=0.0, blank=True, null=True)
    
    # User and Error Information
    user_upload = models.CharField(max_length=50, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    api_response_code = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        unique_together = ['pro_id', 'dis_id', 'upload_month']
        indexes = [
            models.Index(fields=['upload_month', 'status']),
            models.Index(fields=['pro_id', 'dis_id']),
        ]
        verbose_name = 'Water Upload Tracking'
        verbose_name_plural = 'Water Upload Trackings'
    
    def __str__(self):
        return f"{self.pro_name} - {self.dis_name} ({self.upload_month}) - {self.status}"
    
    def calculate_duration(self):
        """Calculate upload duration if both timestamps exist"""
        if self.upload_started and self.upload_completed:
            duration = (self.upload_completed - self.upload_started).total_seconds()
            self.upload_duration = duration
            return duration
        return None
    
    def calculate_success_rate(self):
        """Calculate success rate based on processed vs total records"""
        if self.total_records > 0:
            self.success_rates = (self.processed_records / self.total_records) * 100
            return self.success_rates
        return 0.0
    
    @property
    def is_uploaded_this_month(self):
        """Check if uploaded in current month"""
        current_month = timezone.now().strftime('%Y%m')
        return self.upload_month == current_month and self.status == 'completed'


class WaterUploadLog(models.Model):
    """
    Log entries for upload tracking
    Records all events during upload process
    """
    LOG_LEVEL_CHOICES = [
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
        ('SUCCESS', 'Success')
    ]
    
    tracking = models.ForeignKey(
        WaterUploadDataTracking, 
        on_delete=models.CASCADE, 
        related_name='logs'
    )
    log_level = models.CharField(max_length=10, choices=LOG_LEVEL_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Water Upload Log'
        verbose_name_plural = 'Water Upload Logs'
    
    def __str__(self):
        return f"{self.log_level} - {self.message[:50]}"
# Additional utility model for API configuration (optional)
class WaterSupplyAPIConfig(models.Model):
    """Model to store water supply API configuration"""
    
    name = models.CharField(max_length=100, unique=True)
    api_base_url = models.URLField()
    api_endpoint_template = models.CharField(
        max_length=255,
        help_text="API endpoint template with {month} placeholder"
    )
    
    # Authentication settings
    auth_type = models.CharField(
        max_length=20,
        choices=[
            ('bearer', 'Bearer Token'),
            ('api_key', 'API Key'),
            ('basic', 'Basic Auth')
        ],
        default='bearer'
    )
    
    # Request settings
    timeout_seconds = models.IntegerField(default=300)
    max_retries = models.IntegerField(default=3)
    
    # Status and metadata
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"Water API Config: {self.name}"
    
    def get_api_url(self, month):
        """Get full API URL for a given month"""
        return f"{self.api_base_url.rstrip('/')}/{self.api_endpoint_template.format(month=month)}"