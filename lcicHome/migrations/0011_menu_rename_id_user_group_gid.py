# Generated by Django 4.0.5 on 2022-07-25 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0010_user_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('MID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(max_length=150)),
                ('nameE', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameField(
            model_name='user_group',
            old_name='id',
            new_name='GID',
        ),
    ]
