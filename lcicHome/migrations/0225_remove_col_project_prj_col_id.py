# Generated by Django 5.0.6 on 2024-09-09 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0224_col_project_prj_col_id_col_project_prj_loan_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='col_project_prj',
            name='col_id',
        ),
    ]
