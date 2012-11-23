# -*- encoding: utf-8 -*-
"""
Forms and validation code for user registration.

"""


from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

from coolway_website.models.company import Company
from .models import SEX_CHOICES

attrs_dict = {'class': 'required'}


class RegistrationForm(forms.Form):
    username = forms.EmailField(required=True,
                label=_("Your account email"),
                error_messages={
                    'required': _("You cannot leave this field blank"),
                    'invalid': _('please enter a valid email address'),
                    }
                )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password"))
   

    def clean_username(self):
        username = self.cleaned_data['username']
        emailsuffix = '@%s'%(username.split('@')[1])
        if emailsuffix not in Company.objects.openDomains():
            raise forms.ValidationError(_("not open register for your company,please apply"))
       
        if User.objects.filter(email__iexact=username):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return username
   

class UserProfile(forms.Form):
    sex = forms.ChoiceField(widget=forms.Select(attrs=attrs_dict), choices=SEX_CHOICES,label="sex")
    photos = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea(attrs=attrs_dict),label=_("description"))
    nickname = forms.CharField(required=True,
                label=_("nickname"),
                error_messages={
                    'required': _("nickname field blank")
                    }
                )
    def clean(self):
        return self.cleaned_data