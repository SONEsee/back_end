# Generated by Django 5.0.6 on 2024-09-09 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0190_c1_loan_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c1',
            name='col_id',
        ),
        migrations.RemoveField(
            model_name='c1_disptes',
            name='col_id',
        ),
    ]