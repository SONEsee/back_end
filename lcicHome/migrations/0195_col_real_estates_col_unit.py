# Generated by Django 5.0.6 on 2024-09-09 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0194_col_real_estates_plot_vilid'),
    ]

    operations = [
        migrations.AddField(
            model_name='col_real_estates',
            name='col_unit',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]