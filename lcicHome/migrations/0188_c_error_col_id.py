# Generated by Django 5.0.6 on 2024-09-09 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0187_remove_c_error_col_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_error',
            name='col_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
