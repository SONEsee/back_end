# Generated by Django 5.0.6 on 2024-09-09 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0186_rename_collateral_id_c1_col_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_error',
            name='col_id',
        ),
    ]