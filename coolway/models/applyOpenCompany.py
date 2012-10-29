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