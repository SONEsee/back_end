# Generated by Django 4.1 on 2023-08-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0081_bank_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_branch',
            name='bnk_code',
            field=models.CharField(max_length=10),
        ),
    ]
