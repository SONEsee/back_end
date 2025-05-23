# Generated by Django 4.2 on 2025-04-21 03:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0013_bank_bnk_bnk_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemuser',
            options={},
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='bnk_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='branch_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='insertDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='roles',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterModelTable(
            name='systemuser',
            table='system_user',
        ),
    ]
