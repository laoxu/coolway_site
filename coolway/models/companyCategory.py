
from django.db import models

class CompanyCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField()
    category_id = models.IntegerField()
    status = models.CharField(max_length=15, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'company_category'