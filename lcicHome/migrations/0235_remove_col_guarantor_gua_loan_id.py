# Generated by Django 5.0.6 on 2024-09-09 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0234_col_vechicle_veh_loan_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='col_guarantor_gua',
            name='loan_id',
        ),
    ]
