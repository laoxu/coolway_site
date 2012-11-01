from django.db import models

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