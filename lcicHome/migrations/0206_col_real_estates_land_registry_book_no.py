# Generated by Django 5.0.6 on 2024-09-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0205_remove_col_real_estates_land_registry_book_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='col_real_estates',
            name='land_registry_book_no',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
