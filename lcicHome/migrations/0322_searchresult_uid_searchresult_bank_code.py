# Generated by Django 5.0.6 on 2025-01-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0321_search_batfile_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='UID',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchresult',
            name='bank_code',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
