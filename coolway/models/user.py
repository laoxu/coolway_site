# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, blank=True)
    password = models.CharField(max_length=192, blank=True)
    email = models.CharField(max_length=384, blank=True)
    sex = models.CharField(max_length=18, blank=True)
    status = models.CharField(max_length=24, blank=True)
    photos = models.CharField(max_length=1536, blank=True)
    address = models.CharField(max_length=768, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'user'
