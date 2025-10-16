# utility/tasks.py
from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone
from datetime import datetime

logger = get_task_logger(__name__)

@shared_task(bind=True, max_retries=3)
def auto_upload_all_provinces(self):
    """
    Your electric upload task - Separate from teammate's tasks
    """
    try:
        logger.info("Starting automatic electric upload...")
        
        # Calculate previous month
        current_date = timezone.now()
        if current_date.month == 1:
            upload_month = f"{current_date.year - 1}12"
        else:
            upload_month = f"{current_date.year}{str(current_date.month - 1).zfill(2)}"
        
        from utility.models import edl_province_code, edl_district_code, UploadDataTracking
        from .views import UploadDataAPIView
        
        provinces = edl_province_code.objects.all()
        logger.info(f"Processing {provinces.count()} provinces for month {upload_month}")
        
        for province in provinces:
            districts = edl_district_code.objects.filter(pro_id=province.pro_id)
            
            for district in districts:
                # Create tracking record
                tracking, created = UploadDataTracking.objects.get_or_create(
                    pro_id=district.pro_id,
                    dis_id=district.dis_id,
                    upload_month=upload_month,
                    defaults={
                        'pro_name': province.pro_name,
                        'dis_name': district.dis_name,
                        'status': 'pending',
                        'user_upload': 'AUTO_SYSTEM'
                    }
                )
                
                # Upload data
                try:
                    upload_view = UploadDataAPIView()
                    result = upload_view.fetch_and_process_data(tracking)
                    logger.info(f"✓ {district.dis_name}: Success")
                except Exception as e:
                    logger.error(f"✗ {district.dis_name}: {str(e)}")
        
        logger.info("Auto-upload completed successfully")
        return {'status': 'success', 'month': upload_month}
        
    except Exception as exc:
        logger.error(f"Auto-upload failed: {str(exc)}")
        raise self.retry(exc=exc)
    
    
from celery import shared_task, group
from celery.utils.log import get_task_logger
from django.utils import timezone
from utility.models import UploadDataTracking, UploadLog, edl_province_code, edl_district_code
from lcicHome.views import UploadDataAPIView

logger = get_task_logger(__name__)

@shared_task(bind=True)
def upload_all_provinces_districts(self, upload_month, username='system'):
    """
    Upload ALL provinces and districts for a specific month
    This is the main task that orchestrates the entire upload
    """
    try:
        logger.info(f"🚀 Starting bulk upload for month: {upload_month}")
        
        # Get all provinces
        provinces = edl_province_code.objects.all()
        total_provinces = provinces.count()
        
        logger.info(f"Found {total_provinces} provinces to process")
        
        # Initialize all districts first
        for province in provinces:
            try:
                districts = edl_district_code.objects.filter(pro_id=province.pro_id)
                
                for district in districts:
                    UploadDataTracking.objects.get_or_create(
                        pro_id=district.pro_id,
                        dis_id=district.dis_id,
                        upload_month=upload_month,
                        defaults={
                            'pro_name': province.pro_name,
                            'dis_name': district.dis_name,
                            'status': 'pending',
                            'user_upload': username
                        }
                    )
                
                logger.info(f"✓ Initialized {province.pro_name}: {districts.count()} districts")
                
            except Exception as e:
                logger.error(f"✗ Failed to initialize {province.pro_name}: {str(e)}")
        
        # Queue all district uploads
        all_districts = UploadDataTracking.objects.filter(
            upload_month=upload_month,
            status__in=['pending', 'failed']
        )
        
        total_districts = all_districts.count()
        logger.info(f"Queuing {total_districts} districts for upload...")
        
        # Create a group of tasks for parallel processing
        upload_tasks = []
        for tracking in all_districts:
            task = upload_single_district.si(
                tracking.pro_id,
                tracking.dis_id,
                upload_month,
                username
            )
            upload_tasks.append(task)
        
        # Execute all uploads in parallel (Celery will handle the queue)
        job = group(upload_tasks)
        result = job.apply_async()
        
        logger.info(f"✅ All {total_districts} districts queued for upload!")
        
        return {
            'status': 'success',
            'message': f'Queued {total_districts} districts from {total_provinces} provinces',
            'total_provinces': total_provinces,
            'total_districts': total_districts,
            'upload_month': upload_month
        }
        
    except Exception as exc:
        logger.error(f"Bulk upload failed: {str(exc)}")
        raise self.retry(exc=exc, max_retries=3)


@shared_task(bind=True, max_retries=2)
def upload_single_district(self, province_code, district_code, upload_month, username='system'):
    """
    Upload a single district's data
    This runs in parallel for all districts
    """
    try:
        logger.info(f"📤 Uploading: {province_code}/{district_code} - {upload_month}")
        
        # Get tracking record
        tracking = UploadDataTracking.objects.get(
            pro_id=province_code,
            dis_id=district_code,
            upload_month=upload_month
        )
        
        # Skip if already completed
        if tracking.status == 'completed':
            logger.info(f"⏭️ Skipped {district_code}: Already completed")
            return {'status': 'skipped', 'district': district_code}
        
        # Update status to in_progress
        tracking.status = 'in_progress'
        tracking.upload_started = timezone.now()
        tracking.user_upload = username
        tracking.save()
        
        # Use the existing upload logic
        upload_view = UploadDataAPIView()
        result = upload_view.fetch_and_process_data(tracking)
        
        logger.info(f"✅ Completed {district_code}: {result.get('status', 'done')}")
        
        return {
            'status': 'success',
            'district': district_code,
            'result': result
        }
        
    except Exception as exc:
        logger.error(f"❌ Failed {district_code}: {str(exc)}")
        
        # Update tracking to failed
        try:
            tracking = UploadDataTracking.objects.get(
                pro_id=province_code,
                dis_id=district_code,
                upload_month=upload_month
            )
            tracking.status = 'failed'
            tracking.error_message = str(exc)
            tracking.save()
        except:
            pass
        
        # Retry the task
        raise self.retry(exc=exc, countdown=60)  # Retry after 60 seconds