# Generated by Django 3.2.6 on 2021-08-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0004_h_newscommand_h_newsinfo_h_newstype_h_productinfo_h_protype_h_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='h_newsinfo',
            name='nFiles',
            field=models.FileField(blank=True, null=True, upload_to='uploadNewsFlils'),
        ),
        migrations.AlterField(
            model_name='h_newsinfo',
            name='nimage',
            field=models.FileField(blank=True, null=True, upload_to='uploadNews'),
        ),
    ]
