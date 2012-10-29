from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'',include('coolway.urls')),
)
#handler404 = 'coolway.views.meta.page'
#handler500 = 'coolway.views.meta.error_handler'
