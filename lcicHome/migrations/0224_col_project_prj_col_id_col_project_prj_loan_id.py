# Generated by Django 5.0.6 on 2024-09-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0223_remove_col_project_prj_col_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='col_project_prj',
            name='col_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='col_project_prj',
            name='loan_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]