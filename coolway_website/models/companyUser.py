# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from .company import Company


BELONG_TYPE_COMPANY_USER=u'belong'
CONCERN_TYPE_COMPANY_USER=u'concern'


COMPANY_USER_TYPE_CHOICES = (
    (BELONG_TYPE_COMPANY_USER, u'属于'),
    (CONCERN_TYPE_COMPANY_USER, u'关注'),
)


STATUS_ENABLE = u'enable'
STATUS_DISABLE = u'disable'

STATUS_CHOICES = (
    (STATUS_ENABLE, u'有效'),
    (STATUS_DISABLE, u'无效')
)


class CompanyUserManager(models.Manager):

    def membersCount(self,company):
        '''公司成员数量'''
        return self.members(company).count()

    def members(self,company):
        '''公司成员'''
        return super(CompanyUserManager, self).get_query_set().filter(type=BELONG_TYPE_COMPANY_USER, company=company)


class CompanyUser(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company)
    user = models.ForeignKey(User)
    number = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=21, blank=True, choices=COMPANY_USER_TYPE_CHOICES)
    status = models.CharField(max_length=21, blank=True, choices=STATUS_CHOICES)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)

    objects = CompanyUserManager()


    class Meta:
        db_table = u'company_user'