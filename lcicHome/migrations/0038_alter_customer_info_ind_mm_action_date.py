# Generated by Django 4.1 on 2023-03-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0037_rename_ind_civill_status_customer_info_ind_ind_civil_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_info_ind',
            name='mm_action_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]