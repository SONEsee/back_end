# lcicMain/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab  # ✅ ADD THIS LINE - This was missing!

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lcicMain.settings')

app = Celery('lcicMain')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# ✅ ADD WITHOUT FAIL
app.conf.beat_schedule = {
    # Your electric upload automation
    'auto-upload-electric-data-monthly': {
        'task': 'utility.tasks.auto_upload_all_provinces',
        'schedule': crontab(day_of_month='10', hour=2, minute=0),
        'options': {'expires': 86400},
    },
    # <-- Pherm Code u ni (Automation)
}

app.conf.timezone = 'Asia/Vientiane'  # ✅ ADD THIS
