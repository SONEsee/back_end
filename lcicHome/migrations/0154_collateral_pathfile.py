# Generated by Django 5.0.6 on 2024-08-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0153_remove_collateral_pathfile_collateral_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='collateral',
            name='pathfile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]