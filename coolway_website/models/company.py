
from django.db import models

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    city_id = models.IntegerField()
    area_id = models.IntegerField()
    name = models.CharField(max_length=384, blank=True)
    emailsuffix = models.CharField(max_length=768,unique=True, db_column='emailSuffix', blank=False) # Field name made lowercase.
    image = models.CharField(max_length=768, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'company'