# Generated by Django 3.2.6 on 2021-08-12 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lcicNews', '0006_auto_20210811_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='districtInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(max_length=500)),
                ('nameE', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'DistrictInfo',
            },
        ),
        migrations.CreateModel(
            name='memberType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(max_length=500)),
                ('nameE', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'memberType',
            },
        ),
        migrations.CreateModel(
            name='villageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(max_length=500)),
                ('nameE', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'VillageInfo',
            },
        ),
        migrations.CreateModel(
            name='memberInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('nameL', models.CharField(blank=True, max_length=2500, null=True)),
                ('nameE', models.CharField(blank=True, max_length=2500, null=True)),
                ('descL', models.TextField(blank=True, null=True)),
                ('descE', models.TextField(blank=True, null=True)),
                ('streetInfoL', models.CharField(blank=True, max_length=500, null=True)),
                ('streetInfoE', models.CharField(blank=True, max_length=500, null=True)),
                ('DistrictInfoL', models.CharField(blank=True, max_length=5000, null=True)),
                ('ProvinceInfoL', models.CharField(blank=True, max_length=5000, null=True)),
                ('mImage', models.FileField(blank=True, null=True, upload_to='memberUpload')),
                ('published', models.BooleanField(default=True)),
                ('insertDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('VillageInfoL', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicNews.villageinfo')),
                ('memberType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicNews.membertype')),
            ],
            options={
                'verbose_name_plural': 'memberInfo',
                'ordering': ['code'],
            },
        ),
    ]