# Generated by Django 5.0.6 on 2024-10-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0312_request_charge_bnk_type_searchlog_bnk_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchlog',
            name='inquiry_date',
            field=models.DateTimeField(auto_now_add=True, max_length=10, null=True),
        ),
    ]