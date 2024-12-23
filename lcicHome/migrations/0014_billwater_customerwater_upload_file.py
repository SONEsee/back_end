# Generated by Django 4.1 on 2022-12-23 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lcicNews', '0015_h_lang'),
        ('lcicHome', '0013_alter_login_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillWater',
            fields=[
                ('BillID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.CharField(blank=True, max_length=150)),
                ('SupplyType', models.CharField(max_length=150)),
                ('Outstanding', models.DecimalField(decimal_places=2, max_digits=100)),
                ('BasicTax', models.DecimalField(decimal_places=2, max_digits=100)),
                ('PayAmount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('PaymentID', models.CharField(max_length=150)),
                ('PayType', models.CharField(max_length=150)),
                ('BillOfMonth', models.CharField(max_length=150)),
                ('DateOfIssue', models.DateTimeField(auto_now_add=True)),
                ('PaymentDate', models.DateTimeField(auto_now_add=True)),
                ('districtInfo', models.CharField(blank=True, max_length=150)),
                ('provInfo', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerWater',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.CharField(blank=True, max_length=150)),
                ('CompanyName', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=150)),
                ('Surname', models.CharField(max_length=150)),
                ('NationalID', models.CharField(max_length=150)),
                ('Passport', models.CharField(max_length=150)),
                ('Address', models.CharField(max_length=150)),
                ('districtInfo', models.CharField(blank=True, max_length=150)),
                ('provInfo', models.CharField(blank=True, max_length=150)),
                ('Tel', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=254)),
                ('ConsumerType', models.CharField(max_length=150)),
                ('RegisDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_File',
            fields=[
                ('FID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=255)),
                ('fileUpload', models.FileField(upload_to='')),
                ('fileSize', models.CharField(max_length=255)),
                ('insertDate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=150)),
                ('status_upload', models.CharField(max_length=150)),
                ('GID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicHome.user_group')),
                ('MID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicNews.memberinfo')),
            ],
        ),
    ]
