# Generated by Django 5.0.6 on 2025-01-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0325_searchresult_duplicates_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='duplicates',
            field=models.TextField(),
        ),
    ]
