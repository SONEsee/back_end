# Generated by Django 5.0.6 on 2024-09-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0262_remove_col_vechicle_veh_vehicle_value_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='col_money_mia',
            old_name='mia_owner_gender',
            new_name='owner_gender',
        ),
        migrations.RenameField(
            model_name='col_money_mia',
            old_name='mia_owner_lao_name',
            new_name='owner_lao_name',
        ),
        migrations.RenameField(
            model_name='col_money_mia',
            old_name='mia_owner_lao_surname',
            new_name='owner_lao_surname',
        ),
        migrations.RenameField(
            model_name='col_money_mia',
            old_name='mia_owner_name',
            new_name='owner_name',
        ),
        migrations.RenameField(
            model_name='col_money_mia',
            old_name='mia_owner_surname',
            new_name='owner_surname',
        ),
        migrations.RenameField(
            model_name='col_money_mia',
            old_name='mia_status',
            new_name='status',
        ),
    ]
