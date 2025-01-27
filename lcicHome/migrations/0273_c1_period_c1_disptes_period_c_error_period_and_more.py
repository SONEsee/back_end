# Generated by Django 5.0.6 on 2024-09-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0272_b1_product_type_b1_monthly_product_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='c1',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c1_disptes',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c_error',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_equipment_eqi',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_goldsilver_gold',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_guarantor_gua',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_money_mia',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_project_prj',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_real_estates',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_vechicle_veh',
            name='period',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
