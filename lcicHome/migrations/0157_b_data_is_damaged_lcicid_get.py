# Generated by Django 5.0.6 on 2024-08-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0156_b_data_is_damaged_com_enterprise_code_get'),
    ]

    operations = [
        migrations.AddField(
            model_name='b_data_is_damaged',
            name='lcicID_get',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]