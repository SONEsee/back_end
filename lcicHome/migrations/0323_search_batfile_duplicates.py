# Generated by Django 5.0.6 on 2025-01-17 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0322_searchresult_uid_searchresult_bank_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_batfile',
            name='duplicates',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
