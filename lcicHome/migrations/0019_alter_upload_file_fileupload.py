# Generated by Django 4.1 on 2023-01-24 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0018_alter_upload_file_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_file',
            name='fileUpload',
            field=models.FileField(upload_to=''),
        ),
    ]
