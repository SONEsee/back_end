# Generated by Django 4.2.4 on 2023-11-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0107_alter_investorinfo_investorname'),
    ]

    operations = [
        migrations.CreateModel(
            name='A2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lcicID', models.CharField(max_length=25, null=True)),
                ('com_enterprise_code', models.CharField(max_length=25)),
                ('segmentType', models.CharField(max_length=10)),
                ('lon_sys_id', models.CharField(max_length=30)),
                ('bnk_code', models.CharField(max_length=10)),
                ('customer_id', models.CharField(max_length=30)),
                ('branch_id', models.CharField(max_length=30)),
                ('loan_id', models.CharField(max_length=30)),
                ('lon_open_date', models.DateField(blank=True)),
                ('lon_exp_date', models.DateField(blank=True)),
                ('lon_ext_date', models.DateField(blank=True, null=True)),
                ('lon_int_rate', models.FloatField(default=0, null=True)),
                ('lon_purpose_code', models.CharField(max_length=30)),
                ('lon_credit_line', models.BigIntegerField(default=0, null=True)),
                ('lon_currency_code', models.CharField(max_length=10)),
                ('lon_outstanding_balance', models.BigIntegerField(default=0, null=True)),
                ('lon_account_no', models.CharField(max_length=30)),
                ('lon_no_days_slow', models.CharField(max_length=30)),
                ('lon_class', models.CharField(max_length=10)),
                ('lon_type', models.CharField(max_length=10)),
                ('lon_term', models.CharField(max_length=25)),
                ('lon_status', models.CharField(max_length=10)),
                ('lon_insert_date', models.DateTimeField(blank=True)),
                ('lon_update_date', models.DateTimeField(blank=True)),
                ('lon_applied_date', models.DateTimeField(blank=True)),
                ('is_disputed', models.BigIntegerField(default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='B1_Daily',
        ),
        migrations.DeleteModel(
            name='B1_Monthly',
        ),
        migrations.DeleteModel(
            name='B1_Yearly',
        ),
        migrations.DeleteModel(
            name='bank_bnk',
        ),
        migrations.DeleteModel(
            name='bank_branch',
        ),
        migrations.DeleteModel(
            name='Enterpise_Info_ID',
        ),
        migrations.DeleteModel(
            name='EnterpriseInfo',
        ),
        migrations.DeleteModel(
            name='InvestorInfo',
        ),
        migrations.DeleteModel(
            name='ISISCode',
        ),
        migrations.DeleteModel(
            name='searchList_Model',
        ),
        migrations.RenameField(
            model_name='b1',
            old_name='com_enterprise_code',
            new_name='enterprise_code',
        ),
        migrations.RenameField(
            model_name='upload_file',
            old_name='FileType',
            new_name='uploadType',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='bnk_code',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='is_disputed',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='lon_applied_date',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='lon_insert_date',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='lon_sys_id',
        ),
        migrations.RemoveField(
            model_name='h_newsinfo',
            name='nFiles',
        ),
        migrations.RemoveField(
            model_name='upload_file',
            name='UType',
        ),
        migrations.AddField(
            model_name='h_newsinfo',
            name='nFilesE',
            field=models.FileField(blank=True, null=True, upload_to='uploadNewsFlils/uploadNewsFlilsE'),
        ),
        migrations.AddField(
            model_name='h_newsinfo',
            name='nFilesL',
            field=models.FileField(blank=True, null=True, upload_to='uploadNewsFlils/uploadNewsFlilsL'),
        ),
        migrations.DeleteModel(
            name='Upload_Type',
        ),
    ]
