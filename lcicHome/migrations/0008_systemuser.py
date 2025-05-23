# Generated by Django 4.2 on 2025-04-04 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0007_enterpriseinfo_lcic_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnk_code', models.CharField(max_length=20)),
                ('branch_code', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('roles', models.CharField(max_length=100)),
                ('nameL', models.CharField(max_length=100)),
                ('nameE', models.CharField(max_length=100)),
                ('surnameL', models.CharField(max_length=100)),
                ('surnameE', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('insertDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'System User',
                'verbose_name_plural': 'System Users',
            },
        ),
    ]
