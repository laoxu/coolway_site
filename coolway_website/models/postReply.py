# -*- encoding: utf-8 -*-

from django.db import models
from .user import User
from .post import Post

POST_REPLY_PUB_STATUS = 'pub'
POST_REPLY_WARN_STATUS = 'warn'
POST_REPLY_DEL_STATUS = 'del'
POST_REPLY_HIDE_STATUS = 'hide'


STATUS_CHOICES = (
    (POST_REPLY_PUB_STATUS,'发布'),
    (POST_REPLY_PUB_STATUS,'警告'),
    (POST_REPLY_PUB_STATUS,'删除'),
    (POST_REPLY_PUB_STATUS,'隐藏')
)

class PostReply(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=768, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=12, blank=True, choices = STATUS_CHOICES)
    quote_reply_id = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    class Meta:
        db_table = u'post_reply'

    def __unicode__(self):
        return u"%s %s" % (self.user_name, self.content)