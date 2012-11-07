from __future__ import absolute_import

from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',

    url(r'^$',
        views.post_list,
        name='post_list'),

    url(r'^(?P<post_id>\d+)/$',
        views.post_detail,
        name = 'post_detail'),

    url(r'^(?P<post_id>\d+)/$',
        views.post_reply,
        name = 'post_reply'),
)

