# Generated by Django 5.0.6 on 2024-09-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0242_col_goldsilver_gold_col_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='col_real_estates',
            name='com_enterprise_code',
            field=models.CharField(max_length=255),
        ),
    ]
