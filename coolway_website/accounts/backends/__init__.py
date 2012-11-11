from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from coolway_website.accounts import signals
from coolway_website.accounts.forms import RegistrationFormUniqueEmail
from coolway_website.accounts.models import RegistrationProfile


class DefaultBackend(object):
 
    def register(self, request, **kwargs):
       
        username, password = '%s%s'%(kwargs['username'],kwargs['company']), kwargs['password1']
        email = username
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def activate(self, request, activation_key):
     
        activated = RegistrationProfile.objects.activate_user(activation_key)
        if activated:
            signals.user_activated.send(sender=self.__class__,
                                        user=activated,
                                        request=request)
        return activated

    def registration_allowed(self, request):
       
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_form_class(self, request):
        return RegistrationFormUniqueEmail

    def post_registration_redirect(self, request, user):
    
        return ('accounts_complete', (), {})

    def post_activation_redirect(self, request, user):
        return ('accounts_activation_complete', (), {})
