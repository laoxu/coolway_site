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

class PostReplyManager(models.Manager):

    def get_visible_by_post(self,postId):
        return self.visible().filter(post=postId)

    def visible(self):
        '''状态为：发布，警告，推荐的回复贴'''
        return super(PostReplyManager, self).get_query_set().filter(status__in=[POST_REPLY_PUB_STATUS,POST_REPLY_WARN_STATUS])

    def deleted(self):
        '''删除的帖子回复列表'''
        return super(PostReplyManager, self).get_query_set().filter(status=POST_REPLY_DEL_STATUS)

    def hide(self):
        '''隐藏的帖子回复列表'''
        return super(PostReplyManager, self).get_query_set().filter(status=POST_REPLY_HIDE_STATUS)

class PostReply(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=768, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=12, blank=True, choices = STATUS_CHOICES)
    quote_reply_id = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    modify_time = models.DateTimeField(null=True, blank=True,auto_now=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    objects = PostReplyManager()

    class Meta:
        db_table = u'post_reply'
        ordering = ['-id', 'modify_time']

    def __unicode__(self):
        return u"%s" % (self.content)