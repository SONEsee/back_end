# Generated by Django 3.2.6 on 2021-08-13 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lcicNews', '0010_auto_20210813_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='documType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(max_length=250)),
                ('nameE', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='documentinfo',
            name='documType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lcicNews.documtype'),
        ),
    ]
