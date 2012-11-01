from django.db import models

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField()
    category_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=768, blank=True)
    title = models.CharField(max_length=768, blank=True)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=27, blank=True)
    authority = models.CharField(max_length=21, blank=True)
    is_top = models.CharField(max_length=3, blank=True)
    reply_num = models.IntegerField(null=True, blank=True)
    favor_num = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    last_reply_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'post'

    def __unicode__(self):
        return self.title or unicode(self.content)