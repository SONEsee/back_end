# Generated by Django 5.0.6 on 2024-10-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicNews', '0025_alter_memberinfo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
