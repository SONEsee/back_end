# Generated by Django 5.0.6 on 2024-10-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0308_request_charge_lon_purpose'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(blank=True, null=True)),
                ('Prov_ID', models.CharField(blank=True, max_length=255, null=True)),
                ('Dstr_ID', models.CharField(blank=True, max_length=255, null=True)),
                ('District_Name', models.CharField(blank=True, max_length=2500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prov_ID', models.CharField(blank=True, max_length=50, null=True)),
                ('Province_Name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(blank=True, null=True)),
                ('Prov_ID', models.CharField(blank=True, max_length=255, null=True)),
                ('Dstr_ID', models.CharField(blank=True, max_length=255, null=True)),
                ('Vill_ID', models.CharField(blank=True, max_length=255, null=True)),
                ('Village_Name', models.CharField(blank=True, max_length=2500, null=True)),
            ],
        ),
    ]
