# Generated by Django 4.2.4 on 2023-11-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0100_remove_investorinfo_isiscodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='investorinfo',
            name='IsisCodes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]