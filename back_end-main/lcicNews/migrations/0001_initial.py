# Generated by Django 3.2.6 on 2021-08-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('nameE', models.CharField(blank=True, max_length=100, null=True)),
                ('nameL', models.CharField(blank=True, max_length=100, null=True)),
                ('descE', models.TextField(blank=True, null=True)),
                ('descL', models.TextField(blank=True, null=True)),
                ('nimage', models.FileField(blank=True, null=True, upload_to='upload')),
                ('published', models.BooleanField(default=False)),
                ('insertDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]