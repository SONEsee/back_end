# Generated by Django 5.0.6 on 2024-08-05 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0149_b1_monthly_status_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='b1_monthly',
            name='status_customer',
        ),
    ]