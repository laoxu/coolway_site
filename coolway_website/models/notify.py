from django.db import models

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