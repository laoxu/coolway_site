from __future__ import absolute_import

from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
    # url(r'^(?P<company_id>[-\w]+)/',
    #     views.post_list,
    #     name = 'post-list'
    # ),
    url(r'^list/$',
        views.post_list,
        name='post_list'),

    url(r'^create/(?P<post_id>\d+)$',
        views.post_create,
        name = 'post_create'
    ),
    url(r'^/(\d+)/$',
        views.post_detail,
        name = 'post_detail'),
    # url(
    #     r'^(?P<feed_type_slug>[-\w]+)/$',
    #     views.post_detail,
    #     name = "community-feed-list"
    # ),
    # url(
    #     r'^add/(?P<feed_type_slug>[-\w]+)/$',
    #     views.add_feed,
    #     name = 'community-add-feed'
    # ),
    # url(
    #     r'^edit/(?P<feed_id>\d+)/$',
    #     views.edit_feed,
    #     name = 'community-edit-feed'
    # ),
    # url(
    #     r'^delete/(?P<feed_id>\d+)/$',
    #     views.delete_feed,
    #     name = 'community-delete-feed'
    # ),
)

