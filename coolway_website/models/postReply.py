from django.db import models

class PostReply(models.Model):
    id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=768, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=12, blank=True)
    quote_reply_id = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    modify_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'post_reply'