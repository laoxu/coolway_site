# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views as forum_views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^save/$', forum_views.save_post,name='save_post'),
    url(r'^list/$', forum_views.post_list,name='post_list'),
)
