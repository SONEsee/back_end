# Generated by Django 4.2.4 on 2023-11-17 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0108_a2_delete_b1_daily_delete_b1_monthly_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_bnk',
            fields=[
                ('bnk_sys_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnk_code', models.CharField(max_length=10)),
                ('bnk_short_form', models.CharField(max_length=10)),
                ('bnk_name', models.CharField(max_length=100)),
                ('bnk_lao_name', models.TextField()),
                ('bnk_insert_date', models.DateField(blank=True, null=True)),
                ('bnk_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bank_branch',
            fields=[
                ('branch_sys_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnk_code', models.CharField(max_length=10)),
                ('branch_id', models.CharField(max_length=15)),
                ('branch_name', models.CharField(max_length=50)),
                ('Vill', models.CharField(max_length=50)),
                ('Dis', models.CharField(max_length=50)),
                ('Province', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EnterpriseInfo',
            fields=[
                ('LCICID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnterpriseID', models.CharField(blank=True, max_length=50, null=True)),
                ('enterpriseNameLao', models.CharField(blank=True, max_length=255, null=True)),
                ('eneterpriseNameEnglish', models.CharField(blank=True, max_length=255, null=True)),
                ('regisCertificateNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('regisDate', models.DateTimeField(blank=True, null=True)),
                ('enLocation', models.CharField(blank=True, max_length=50, null=True)),
                ('regisStrationOfficeType', models.CharField(blank=True, max_length=50, null=True)),
                ('regisStationOfficeCode', models.CharField(blank=True, max_length=50, null=True)),
                ('enLegalStrature', models.CharField(blank=True, max_length=500, null=True)),
                ('foreigninvestorFlag', models.CharField(blank=True, max_length=500, null=True)),
                ('investmentAmount', models.FloatField(blank=True, null=True)),
                ('investmentCurrency', models.CharField(blank=True, max_length=50, null=True)),
                ('representativeNationality', models.CharField(blank=True, max_length=50, null=True)),
                ('LastUpdate', models.DateTimeField(blank=True, null=True)),
                ('CancellationDate', models.DateTimeField(blank=True, null=True)),
                ('InsertDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdateDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorInfo',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnterpriseID', models.CharField(blank=True, max_length=50, null=True)),
                ('investorName', models.CharField(blank=True, max_length=255, null=True)),
                ('investorOwnerPercentage', models.CharField(blank=True, max_length=100, null=True)),
                ('investorNationality', models.CharField(blank=True, max_length=50, null=True)),
                ('investorcardNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('investorMobile', models.CharField(blank=True, max_length=50, null=True)),
                ('InsertDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdateDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ISISCode',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnterpriseID', models.CharField(blank=True, max_length=50, null=True)),
                ('IsisCodes', models.CharField(blank=True, max_length=255, null=True)),
                ('IsisName', models.CharField(blank=True, max_length=4000, null=True)),
                ('InsertDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdateDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UType', models.CharField(max_length=3)),
                ('nameL', models.CharField(max_length=50)),
                ('nameE', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='A2',
        ),
        migrations.DeleteModel(
            name='B1',
        ),
        migrations.AlterModelOptions(
            name='h_lang',
            options={'verbose_name_plural': 'H_Lang'},
        ),
        migrations.RenameField(
            model_name='upload_file',
            old_name='uploadType',
            new_name='FileType',
        ),
        migrations.AddField(
            model_name='upload_file',
            name='UType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicHome.upload_type'),
        ),
    ]