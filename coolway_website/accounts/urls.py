
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from views import activate
from views import register
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
                       url(r'^login/$',
                           auth_views.login,
                           {'template_name': 'accounts/login.html'},
                           name='auth_login'),
                       url(r'^logout/$',
                           auth_views.logout,
                           {'template_name': 'accounts/logout.html'},
                           name='auth_logout'),
                       url(r'^password/change/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^password/change/done/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^password/reset/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^password/reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
                       url(r'^activate/complete/$',
                           direct_to_template,
                           {'template': 'accounts/activation_complete.html'},
                           name='accounts_activation_complete'),
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^activate/(?P<activation_key>\w+)/$',
                           activate,
                           {'backend': 'coolway_website.accounts.backends.DefaultBackend'},
                           name='accounts_activate'),
                       url(r'^register/$',
                           register,
                           {'backend': 'coolway_website.accounts.backends.DefaultBackend'},
                           name='accounts_register'),
                       url(r'^register/complete/$',
                           direct_to_template,
                           {'template': 'accounts/registration_complete.html'},
                           name='accounts_complete'),
                       url(r'^register/closed/$',
                           direct_to_template,
                           {'template': 'accounts/registration_closed.html'},
                           name='accounts_disallowed'),
                      )