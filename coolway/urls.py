# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from coolway.views import hellodj
from coolway.views.meta import new_city

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', hellodj.index,name='index'),
    url(r'^hello/$',hellodj.hello,name='hello'),
    url(r'^time/plus/(\d{1,2})/$',hellodj.hours_ahead,name='hours_ahead'),
    url(r'^new_city/$',new_city),
)
