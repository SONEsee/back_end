# Generated by Django 4.2.4 on 2023-11-10 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0099_enterpise_info_id_searchlist_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investorinfo',
            name='IsisCodes',
        ),
    ]
