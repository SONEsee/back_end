# Generated by Django 4.1 on 2023-08-22 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0073_upload_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_file',
            name='UType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicHome.upload_type'),
        ),
    ]
