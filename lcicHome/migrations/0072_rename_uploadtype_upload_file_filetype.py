# Generated by Django 4.1 on 2023-08-22 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0071_b1_daily_b1_monthly_b1_yearly'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_file',
            old_name='uploadType',
            new_name='FileType',
        ),
    ]