# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ApplyOpenCompany(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=768, blank=True)
    city_id = models.IntegerField()
    area_id = models.IntegerField()
    email = models.CharField(max_length=12288, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'apply_open_company'

class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, blank=True)
    city_id = models.IntegerField()
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'area'

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'category'

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'city'

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    city_id = models.IntegerField()
    area_id = models.IntegerField()
    name = models.CharField(max_length=384, blank=True)
    emailsuffix = models.CharField(max_length=768, db_column='emailSuffix', blank=True) # Field name made lowercase.
    image = models.CharField(max_length=768, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'company'

class CompanyCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField()
    category_id = models.IntegerField()
    status = models.CharField(max_length=15, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'company_category'

class CompanyUser(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=384, blank=True)
    number = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=21, blank=True)
    status = models.CharField(max_length=21, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'company_user'

class Friend(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    friend_id = models.CharField(max_length=384, blank=True)
    status = models.CharField(max_length=21, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'friend'

class Invite(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    invitee = models.CharField(max_length=384, blank=True)
    code = models.CharField(max_length=384, blank=True)
    status = models.CharField(max_length=24, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'invite'

class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    to_user_id = models.IntegerField()
    content = models.CharField(max_length=12288, blank=True)
    status = models.CharField(max_length=18, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'message'

class Notify(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    type = models.CharField(max_length=21, blank=True)
    to_user_id = models.IntegerField()
    content = models.CharField(max_length=12288, blank=True)
    status = models.CharField(max_length=18, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'notify'

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField()
    category_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=768, blank=True)
    title = models.CharField(max_length=768, blank=True)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=27, blank=True)
    authority = models.CharField(max_length=21, blank=True)
    is_top = models.CharField(max_length=3, blank=True)
    reply_num = models.IntegerField(null=True, blank=True)
    favor_num = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    last_reply_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'post'

class PostReply(models.Model):
    id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=768, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=12, blank=True)
    quote_reply_id = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'post_reply'

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

