# Generated by Django 5.0.6 on 2024-09-20 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0280_rename_user_id_col_guarantor_gua_address_district_eng_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='col_guarantor_com',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_file', models.CharField(max_length=100)),
                ('period', models.CharField(max_length=150)),
                ('lcicID', models.CharField(max_length=30)),
                ('com_enterprise_code', models.CharField(max_length=100)),
                ('bnk_code', models.CharField(max_length=100)),
                ('col_type', models.CharField(max_length=100)),
                ('bank_customer_ID', models.CharField(max_length=100)),
                ('branch_id_code', models.CharField(max_length=100)),
                ('loan_id', models.CharField(max_length=100)),
                ('col_id', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('value_unit', models.CharField(max_length=100)),
                ('gua_com_status', models.CharField(max_length=100)),
                ('gua_com_insert_date', models.CharField(max_length=100)),
                ('gua_enterprise_code', models.CharField(max_length=100)),
                ('enterprise_regist_date', models.CharField(max_length=100)),
                ('enterprise_regist_place', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('company_lao_name', models.CharField(max_length=100)),
                ('enterprise_category', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_surname', models.CharField(max_length=100)),
                ('owner_lao_name', models.CharField(max_length=100)),
                ('owner_lao_surname', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('insert_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
            options={
                'db_table': 'col_guarantor_com',
            },
        ),
    ]
