# Generated by Django 5.0.6 on 2024-07-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcicHome', '0129_alter_b1_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b1',
            name='id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]