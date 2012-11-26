from django.conf.urls import patterns, include, url
from django.conf import settings
from coolway_website.views import *
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', index,name='index'),
    url(r'^accounts/',include('coolway_website.accounts.urls')),
    url(r'^post/',include('coolway_website.post.urls')),
    (r'^upload/', include('coolway_website.fileupload.urls')),
    url(r'^images/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),

)
#handler404 = 'coolway.views.meta.page'
#handler500 = 'coolway.views.meta.error_handler'
