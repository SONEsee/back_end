# Generated by Django 5.0.6 on 2024-09-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0237_remove_col_guarantor_gua_col_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='col_guarantor_gua',
            name='col_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]