# -*- encoding: utf-8 -*-
"""
Forms and validation code for user registration.

"""


from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

from coolway_website.models.company import Company

attrs_dict = {'class': 'required'}


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password (again)"))
    openCompanys = Company.objects.all()
    company = forms.ChoiceField(widget=forms.Select(attrs=attrs_dict), choices=[(company.emailsuffix,company.name) for company in openCompanys],label="choose company")
    
    def clean_username(self):
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']


class RegistrationFormUniqueEmail(RegistrationForm):

    openCompanys = Company.objects.all();

    open_domains = range(0)

    for company in openCompanys:
        open_domains.append(company.emailsuffix)

    def clean(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        email_domain = self.cleaned_data['email'].split('@')[1]

        if  self.cleaned_data['company'] !=  email_domain:
            raise forms.ValidationError(_("input correct email"))

        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data

        # 这里跳转到公司注册申请页面
        if email_domain not in self.open_domains:
            raise forms.ValidationError(_("not open register for your company,please apply"))

        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']