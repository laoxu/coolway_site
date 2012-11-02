# -*- encoding: utf-8 -*-
from django.db import models
from .user import User
from .company import Company
from .category import Category


DRAFT_STATUS_POST='draft'
PUB_STATUS_POST='pub'
WARN_STATUS_POST='warn'
DEL_STATUS_POST='del'
RECOMMEND_STATUS_POST='recommend'
HIDE_STATUS_POST='hide'

STATUS_CHOICES = (
    (DRAFT_STATUS_POST, '草稿'),
    (PUB_STATUS_POST, '发布'),
    (WARN_STATUS_POST, '警告'),
    (DEL_STATUS_POST, '删除'),
    (RECOMMEND_STATUS_POST, '推荐'),
    (HIDE_STATUS_POST, '隐藏')
)

PUBLIC_AUTHORITY_POST = 'public'
COMPANY_AUTHORITY_POST ='company'

AUTHORITY_CHOICES = (
    (PUBLIC_AUTHORITY_POST,'公开'),
    (COMPANY_AUTHORITY_POST,'公司')
)



class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=768, blank=True)
    title = models.CharField(max_length=768, blank=True)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=27, blank=True,choices=STATUS_CHOICES)
    authority = models.CharField(max_length=21, blank=True, choices=AUTHORITY_CHOICES)
    is_top = models.CharField(max_length=3, blank=True)
    reply_num = models.IntegerField(null=True, blank=True)
    favor_num = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    last_reply_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    company = models.ForeignKey(Company)

    class Meta:
        db_table = u'post'

    def __unicode__(self):
        return u"%s %s" % (self.title, self.content)