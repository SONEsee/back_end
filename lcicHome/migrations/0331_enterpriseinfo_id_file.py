# Generated by Django 5.0.6 on 2025-01-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0330_enterpriseinfo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpriseinfo',
            name='id_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]