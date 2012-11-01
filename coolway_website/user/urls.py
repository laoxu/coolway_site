# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views as user_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', user_views.user_page,name='user_page'),
    url(r'^hello/$',user_views.hello,name='hello'),
    url(r'^time/plus/(\d{1,2})/$',user_views.hours_ahead,name='hours_ahead'),
)
