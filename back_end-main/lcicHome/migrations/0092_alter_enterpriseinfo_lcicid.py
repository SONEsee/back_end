# Generated by Django 4.1 on 2023-09-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0091_enterpriseinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseinfo',
            name='LCICID',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]