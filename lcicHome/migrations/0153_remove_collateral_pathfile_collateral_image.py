# Generated by Django 5.0.6 on 2024-08-15 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0152_disputes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collateral',
            name='pathfile',
        ),
        migrations.AddField(
            model_name='collateral',
            name='image',
            field=models.ImageField(default=1, upload_to='collateral_images/'),
            preserve_default=False,
        ),
    ]
