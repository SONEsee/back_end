# Generated by Django 5.0.6 on 2025-01-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0329_uploadfile_enterpriseinfo_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpriseinfo',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]