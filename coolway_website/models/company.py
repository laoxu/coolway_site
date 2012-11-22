# -*- encoding: utf-8 -*-
from django.db import models

BELONG_TYPE_COMPANY_USER=u'belong'

class CompanyManager(models.Manager):

    def openDomains(self):
        '''获得开通公司邮箱后缀列表'''
        open_domains = range(0)

        for company in self.all():
            open_domains.append(company.emailsuffix)
        return open_domains

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    city_id = models.IntegerField()
    area_id = models.IntegerField()
    name = models.CharField(max_length=384, blank=True)
    emailsuffix = models.CharField(max_length=768,unique=True, db_column='emailSuffix', blank=False) # Field name made lowercase.
    image = models.CharField(max_length=768, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)

    objects = CompanyManager()

    class Meta:
        db_table = u'company'

    def members(self):
        return self.companyuser_set.filter(type=BELONG_TYPE_COMPANY_USER)

    def membersCount(self):
        return self.members().count()

    def getNextMemberNum(self):
        return self.membersCount()+1