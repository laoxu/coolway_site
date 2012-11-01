from django.db import models

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