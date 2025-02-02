# Generated by Django 5.0.6 on 2024-08-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0169_col_real_estates'),
    ]

    operations = [
        migrations.CreateModel(
            name='col_goldsilver_gold',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lcicID', models.CharField(max_length=30)),
                ('com_enterprise_code', models.CharField(max_length=30)),
                ('bank_customer_ID', models.CharField(max_length=30)),
                ('branch_id_code', models.CharField(max_length=30)),
                ('loan_id', models.CharField(max_length=30)),
                ('collateral_id', models.CharField(max_length=30)),
                ('weight', models.CharField(max_length=30)),
                ('unit', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('insert_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
            options={
                'db_table': 'col_goldsilver_gold',
            },
        ),
        migrations.CreateModel(
            name='col_guarantor_gua',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lcicID', models.CharField(max_length=30)),
                ('com_enterprise_code', models.CharField(max_length=30)),
                ('bank_customer_ID', models.CharField(max_length=30)),
                ('branch_id_code', models.CharField(max_length=30)),
                ('loan_id', models.CharField(max_length=30)),
                ('collateral_id', models.CharField(max_length=30)),
                ('guarantor_type', models.CharField(max_length=30)),
                ('guarantor_nationality', models.CharField(max_length=30)),
                ('national_id', models.CharField(max_length=30)),
                ('national_expiry_date', models.CharField(max_length=30)),
                ('passport', models.CharField(max_length=30)),
                ('passport_expiry_date', models.CharField(max_length=30)),
                ('familybook', models.CharField(max_length=30)),
                ('familybook_province_code_of_issue', models.CharField(max_length=30)),
                ('familybook_issue_date', models.CharField(max_length=30)),
                ('birthdate', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('ist_name_english', models.CharField(max_length=30)),
                ('ist_name_lao', models.CharField(max_length=30)),
                ('nickname_english', models.CharField(max_length=30)),
                ('nickname_lao', models.CharField(max_length=30)),
                ('surname_english', models.CharField(max_length=30)),
                ('surname_lao', models.CharField(max_length=30)),
                ('address_number_street_english', models.CharField(max_length=30)),
                ('address_number_street_lao', models.CharField(max_length=30)),
                ('address_village_english', models.CharField(max_length=30)),
                ('address_village_lao', models.CharField(max_length=30)),
                ('address_sub_district_english', models.CharField(max_length=30)),
                ('address_sub_district_lao', models.CharField(max_length=30)),
                ('address_district_english', models.CharField(max_length=30)),
                ('address_district_lao', models.CharField(max_length=30)),
                ('address_province_code', models.CharField(max_length=30)),
                ('enterprise_code', models.CharField(max_length=30)),
                ('registration_date_of_issue', models.CharField(max_length=30)),
                ('registration_place_issue', models.CharField(max_length=30)),
                ('company_name_english', models.CharField(max_length=30)),
                ('company_name_lao', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('insert_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
            options={
                'db_table': 'col_guarantor_gua',
            },
        ),
        migrations.CreateModel(
            name='col_vechicle_veh',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lcicID', models.CharField(max_length=30)),
                ('com_enterprise_code', models.CharField(max_length=30)),
                ('bank_customer_ID', models.CharField(max_length=30)),
                ('branch_id_code', models.CharField(max_length=30)),
                ('loan_id', models.CharField(max_length=30)),
                ('collateral_id', models.CharField(max_length=30)),
                ('name_owner', models.CharField(max_length=30)),
                ('plate_number', models.CharField(max_length=30)),
                ('engine_number', models.CharField(max_length=30)),
                ('body_numbe', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('insert_date', models.DateField()),
                ('update_date', models.DateField()),
            ],
            options={
                'db_table': 'col_vechicle_veh',
            },
        ),
    ]
