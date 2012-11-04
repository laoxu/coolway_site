from django.conf.urls import patterns, include, url
from coolway_website.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', index,name='index'),
    url(r'^user/',include('coolway_website.accounts.urls')),
    url(r'^post/',include('coolway_website.forum.urls')),
)
#handler404 = 'coolway.views.meta.page'
#handler500 = 'coolway.views.meta.error_handler'
