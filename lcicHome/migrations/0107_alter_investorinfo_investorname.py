# Generated by Django 4.2.4 on 2023-11-13 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0106_investorinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorinfo',
            name='investorName',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
