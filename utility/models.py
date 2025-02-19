# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import os

def json_upload_path(instance, filename):
    return os.path.join('json_uploads', filename)

class JsonfileWater(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_path = models.FileField(upload_to=json_upload_path)  # File upload field
    insertDate = models.DateTimeField(auto_now_add=True, blank=True)
    updateDate = models.DateTimeField(auto_now=True, blank=True)
    status = models.CharField(max_length=20)
    user_upload = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'Jsonfile_water'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Test(models.Model):
    name_lcic = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'test'
