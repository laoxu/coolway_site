from django.db import models
from django.contrib.auth.models import User

from .company import Company

class CompanyUser(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company)
    user = models.ForeignKey(User)
    number = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=21, blank=True)
    status = models.CharField(max_length=21, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'company_user'