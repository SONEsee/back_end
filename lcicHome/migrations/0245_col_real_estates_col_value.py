# Generated by Django 5.0.6 on 2024-09-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0244_alter_c1_com_enterprise_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='col_real_estates',
            name='col_value',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]