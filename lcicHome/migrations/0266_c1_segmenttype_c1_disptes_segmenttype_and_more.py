# Generated by Django 5.0.6 on 2024-09-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0265_rename_project_namber_col_project_prj_project_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='c1',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c1_disptes',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c_error',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_equipment_eqi',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_goldsilver_gold',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_guarantor_gua',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_money_mia',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_project_prj',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_real_estates',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_vechicle_veh',
            name='segmentType',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]