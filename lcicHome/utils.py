from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    """
    Generate JWT tokens for a custom user model (LCICSystemUser).
    """
    refresh = RefreshToken()
    
 
    refresh['user_id'] = user.id  
    
    
    refresh['username'] = user.username
    refresh['roles'] = user.roles
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
# API Edl Tracking:
# utils.py - Data validation and processing utilities

from decimal import Decimal, InvalidOperation
from datetime import datetime
import re
from django.core.exceptions import ValidationError

class ElectricBillValidator:
    """Utility class for validating electric bill data"""
    
    REQUIRED_FIELDS = [
        'MASTER_BILL_ID', 'INDEX_NO', 'PROVINCE_CODE', 'DIS_ID'
    ]
    
    NUMERIC_FIELDS = [
        'OUTSTANDING', 'BILL_AMOUNT', 'FACT_TOTAL'
    ]
    
    DATE_PATTERN = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    MONTH_PATTERN = re.compile(r'^\d{2}-\d{4}$')
    
    @classmethod
    def validate_record(cls, record, expected_province=None, expected_district=None):
        """
        Validate a single electric bill record
        
        Args:
            record: Dictionary containing electric bill data
            expected_province: Expected province code for validation
            expected_district: Expected district code for validation
            
        Returns:
            dict: {
                'is_valid': bool,
                'errors': list of error messages,
                'warnings': list of warning messages
            }
        """
        errors = []
        warnings = []
        
        # Check required fields
        for field in cls.REQUIRED_FIELDS:
            if not record.get(field):
                errors.append(f"Missing required field: {field}")
        
        # Validate numeric fields
        for field in cls.NUMERIC_FIELDS:
            value = record.get(field)
            if value is not None:
                try:
                    decimal_value = Decimal(str(value))
                    if decimal_value < 0:
                        warnings.append(f"Negative value in {field}: {value}")
                except (InvalidOperation, ValueError, TypeError):
                    errors.append(f"Invalid numeric value in {field}: {value}")
        
        # Validate province and district codes
        if expected_province and record.get('PROVINCE_CODE') != expected_province:
            errors.append(
                f"Province code mismatch: expected {expected_province}, "
                f"got {record.get('PROVINCE_CODE')}"
            )
        
        if expected_district and record.get('DIS_ID') != expected_district:
            errors.append(
                f"District code mismatch: expected {expected_district}, "
                f"got {record.get('DIS_ID')}"
            )
        
        # Validate date formats
        payment_date = record.get('PAYMENTDAY')
        if payment_date and not cls.DATE_PATTERN.match(str(payment_date)):
            warnings.append(f"Invalid payment date format: {payment_date}")
        
        invoice_date = record.get('INVD')
        if invoice_date and not cls.DATE_PATTERN.match(str(invoice_date)):
            warnings.append(f"Invalid invoice date format: {invoice_date}")
        
        invoice_month = record.get('INVM')
        if invoice_month and not cls.MONTH_PATTERN.match(str(invoice_month)):
            warnings.append(f"Invalid invoice month format: {invoice_month}")
        
        # Validate IDs
        customer_id = record.get('MASTER_BILL_ID')
        if customer_id and len(str(customer_id)) > 255:
            errors.append(f"Customer ID too long: {len(str(customer_id))} characters")
        
        payment_id = record.get('PAYMENT_ID')
        if not payment_id:
            warnings.append("Missing Payment ID")
        
        return {
            'is_valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    @classmethod
    def clean_record(cls, record):
        """
        Clean and normalize record data
        
        Args:
            record: Raw record dictionary
            
        Returns:
            dict: Cleaned record dictionary
        """
        cleaned = {}
        
        # Clean string fields
        string_fields = [
            'MASTER_BILL_ID', 'INDEX_NO', 'SUPPLY_TYPE', 'PAYMENT_ID',
            'PAYMENT_WAY', 'PAYMENTDAY', 'INVM', 'INVD', 'DIS_ID', 'PROVINCE_CODE'
        ]
        
        for field in string_fields:
            value = record.get(field, '')
            cleaned[field] = str(value).strip() if value is not None else ''
        
        # Clean numeric fields
        for field in cls.NUMERIC_FIELDS:
            value = record.get(field, 0)
            try:
                cleaned[field] = Decimal(str(value)) if value else Decimal('0.00')
            except (InvalidOperation, ValueError, TypeError):
                cleaned[field] = Decimal('0.00')
        
        return cleaned


class DataProcessingStats:
    """Utility class for tracking data processing statistics"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset all counters"""
        self.total_records = 0
        self.processed_records = 0
        self.failed_records = 0
        self.duplicate_records = 0
        self.validation_errors = []
        self.processing_start_time = None
        self.processing_end_time = None
    
    def start_processing(self):
        """Mark the start of processing"""
        self.processing_start_time = datetime.now()
        self.reset()
    
    def end_processing(self):
        """Mark the end of processing"""
        self.processing_end_time = datetime.now()
    
    def add_record(self, success=True, is_duplicate=False, errors=None):
        """
        Add a record to the statistics
        
        Args:
            success: Whether the record was processed successfully
            is_duplicate: Whether the record was a duplicate
            errors: List of validation errors (if any)
        """
        self.total_records += 1
        
        if is_duplicate:
            self.duplicate_records += 1
        elif success:
            self.processed_records += 1
        else:
            self.failed_records += 1
            if errors:
                self.validation_errors.extend(errors)
    
    @property
    def success_rate(self):
        """Calculate success rate percentage"""
        if self.total_records == 0:
            return 0
        return (self.processed_records / self.total_records) * 100
    
    @property
    def processing_duration(self):
        """Get processing duration in seconds"""
        if self.processing_start_time and self.processing_end_time:
            return (self.processing_end_time - self.processing_start_time).total_seconds()
        return None
    
    @property
    def records_per_second(self):
        """Calculate records processed per second"""
        duration = self.processing_duration
        if duration and duration > 0:
            return self.total_records / duration
        return None
    
    def get_summary(self):
        """Get a summary of processing statistics"""
        return {
            'total_records': self.total_records,
            'processed_records': self.processed_records,
            'failed_records': self.failed_records,
            'duplicate_records': self.duplicate_records,
            'success_rate': round(self.success_rate, 2),
            'processing_duration': self.processing_duration,
            'records_per_second': round(self.records_per_second, 2) if self.records_per_second else None,
            'total_errors': len(self.validation_errors)
        }


def batch_process_electric_bills(records, tracking, username, batch_size=1000):
    """
    Enhanced batch processing with detailed statistics and validation
    
    Args:
        records: List of electric bill records
        tracking: UploadDataTracking instance
        username: Username for the UserID field
        batch_size: Number of records to process in each batch
        
    Returns:
        dict: Processing results with detailed statistics
    """
    from utility.models import Electric_Bill
    from django.db import transaction
    
    stats = DataProcessingStats()
    stats.start_processing()
    validator = ElectricBillValidator()
    
    batch = []
    
    try:
        with transaction.atomic():
            for i, record in enumerate(records, 1):
                # Validate record
                validation_result = validator.validate_record(
                    record, 
                    expected_province=tracking.pro_id,
                    expected_district=tracking.dis_id
                )
                
                if not validation_result['is_valid']:
                    stats.add_record(success=False, errors=validation_result['errors'])
                    continue
                
                # Clean record data
                cleaned_record = validator.clean_record(record)
                
                # Check for duplicates
                if Electric_Bill.objects.filter(
                    Payment_ID=cleaned_record['PAYMENT_ID'],
                    InvoiceNo=cleaned_record['INDEX_NO'][:255],
                    ProID=tracking.pro_id,
                    DisID=tracking.dis_id
                ).exists():
                    stats.add_record(success=False, is_duplicate=True)
                    continue
                
                # Create Electric_Bill object
                bill = Electric_Bill(
                    Customer_ID=cleaned_record['MASTER_BILL_ID'][:255],
                    InvoiceNo=cleaned_record['INDEX_NO'][:255],
                    TypeOfPro=cleaned_record['SUPPLY_TYPE'][:100],
                    Outstanding=cleaned_record['OUTSTANDING'],
                    Basic_Tax=cleaned_record['FACT_TOTAL'],
                    Bill_Amount=cleaned_record['BILL_AMOUNT'],
                    Debt_Amount=Decimal('0.00'),
                    Payment_ID=cleaned_record['PAYMENT_ID'],
                    PaymentType=cleaned_record['PAYMENT_WAY'],
                    Payment_Date=cleaned_record['PAYMENTDAY'],
                    InvoiceMonth=cleaned_record['INVM'][:50],
                    InvoiceDate=cleaned_record['INVD'][:100],
                    DisID=cleaned_record['DIS_ID'][:100],
                    ProID=cleaned_record['PROVINCE_CODE'][:100],
                    UserID=username
                )
                
                batch.append(bill)
                
                # Process batch when it reaches batch_size
                if len(batch) >= batch_size:
                    Electric_Bill.objects.bulk_create(batch, ignore_conflicts=True)
                    
                    for _ in batch:
                        stats.add_record(success=True)
                    
                    # Update tracking
                    tracking.processed_records = stats.processed_records
                    tracking.failed_records = stats.failed_records
                    tracking.save()
                    
                    batch = []
            
            # Process remaining batch
            if batch:
                Electric_Bill.objects.bulk_create(batch, ignore_conflicts=True)
                for _ in batch:
                    stats.add_record(success=True)
        
        stats.end_processing()
        
        # Final tracking update
        tracking.processed_records = stats.processed_records
        tracking.failed_records = stats.failed_records
        tracking.total_records = stats.total_records
        tracking.save()
        
        return {
            'success': True,
            'statistics': stats.get_summary(),
            'message': f'Processing completed: {stats.processed_records}/{stats.total_records} records processed'
        }
        
    except Exception as e:
        stats.end_processing()
        return {
            'success': False,
            'statistics': stats.get_summary(),
            'error': str(e)
        }