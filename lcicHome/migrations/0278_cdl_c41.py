# Generated by Django 5.0.6 on 2024-09-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0277_cdl_c39_cdl_c40_cdl_id_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdl',
            name='c41',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
