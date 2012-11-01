from django.db import models

class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, blank=True)
    city_id = models.IntegerField()
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'area'