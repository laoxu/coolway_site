# -*- encoding: utf-8 -*-
from django.db import models
from .user import User
from .company import Company
from .category import Category


DRAFT_STATUS_POST=u'draft'
PUB_STATUS_POST=u'pub'
WARN_STATUS_POST=u'warn'
DEL_STATUS_POST=u'del'
RECOMMEND_STATUS_POST=u'recommend'
HIDE_STATUS_POST=u'hide'

STATUS_CHOICES = (
    (DRAFT_STATUS_POST, u'草稿'),
    (PUB_STATUS_POST, u'发布'),
    (WARN_STATUS_POST, u'警告'),
    (DEL_STATUS_POST, u'删除'),
    (RECOMMEND_STATUS_POST, u'推荐'),
    (HIDE_STATUS_POST, u'隐藏')
)

PUBLIC_AUTHORITY_POST = u'public'
COMPANY_AUTHORITY_POST =u'company'

AUTHORITY_CHOICES = (
    (PUBLIC_AUTHORITY_POST,u'公开'),
    (COMPANY_AUTHORITY_POST,u'公司')
)

class PostManager(models.Manager):

    def visible_in_company(self):
        '''只在公司范围可见的帖子'''
        return self.visible().filter(authority=COMPANY_AUTHORITY_POST)

    def visible_public(self):
        '''所有公开的的帖子'''
        return self.visible().filter(authority=PUBLIC_AUTHORITY_POST)

    def visible(self):
        '''帖子状态为：发布，警告，推荐'''
        return super(PostManager, self).get_query_set().filter(status__in=[PUB_STATUS_POST,WARN_STATUS_POST,RECOMMEND_STATUS_POST])

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=768, blank=True,null=True)
    title = models.CharField(max_length=768, blank=False,null=False)
    content = models.TextField(blank=False,null=False)
    status = models.CharField(max_length=27, blank=True,choices=STATUS_CHOICES)
    authority = models.CharField(max_length=21, blank=True, choices=AUTHORITY_CHOICES)
    is_top = models.CharField(max_length=3, blank=True)
    reply_num = models.IntegerField(null=True, blank=True)
    favor_num = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    modify_time = models.DateTimeField(null=True, blank=True,auto_now=True)
    last_reply_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    company = models.ForeignKey(Company)

    objects = PostManager()

    class Meta:
        db_table = u'post'
        ordering = ['-id', 'modify_time']

    def __unicode__(self):
        return u"%s %s" % (self.title, self.content)

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', [str(self.id)])

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
