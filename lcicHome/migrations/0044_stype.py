# Generated by Django 4.1 on 2023-06-19 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0043_b1_customer_info_ind_errors'),
    ]

    operations = [
        migrations.CreateModel(
            name='SType',
            fields=[
                ('SType', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(blank=True, max_length=150)),
                ('nameE', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
