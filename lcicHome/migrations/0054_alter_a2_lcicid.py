# Generated by Django 4.1 on 2023-06-20 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0053_alter_a2_lon_ext_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a2',
            name='lcicID',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
