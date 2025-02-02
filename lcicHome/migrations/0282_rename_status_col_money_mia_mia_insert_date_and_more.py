# Generated by Django 5.0.6 on 2024-09-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0281_col_guarantor_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='col_money_mia',
            old_name='status',
            new_name='mia_insert_date',
        ),
        migrations.AddField(
            model_name='col_equipment_eqi',
            name='machine_insert_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_goldsilver_gold',
            name='gld_insert_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_money_mia',
            name='mia_status',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_project_prj',
            name='project_insert_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_real_estates',
            name='land_insert_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_vechicle_veh',
            name='vehicle_insert_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
