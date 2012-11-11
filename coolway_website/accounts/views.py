# -*- encoding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings

from PIL import Image
import uuid

from ..models.area import Area
from forms import UserProfile
from models import SEX_CHOICES

from . import get_backend

import datetime

@login_required
def user_page(request):
    current_date = datetime.datetime.now()
    return render_to_response('index.html', {'current_date': current_date})


def login():
    pass

def logout():
    pass


def activate(request, backend,
             template_name='accounts/activate.html',
             success_url=None, extra_context=None, **kwargs):

    backend = get_backend(backend)
    account = backend.activate(request, **kwargs)

    if account:
        if success_url is None:
            to, args, kwargs = backend.post_activation_redirect(request, account)
            return redirect(to, *args, **kwargs)
        else:
            return redirect(success_url)

    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(template_name,
                              kwargs,
                              context_instance=context)


def register(request, backend, success_url=None, form_class=None,
             disallowed_url='registration_disallowed',
             template_name='accounts/registration_form.html',
             extra_context=None):

    backend = get_backend(backend)
    if not backend.registration_allowed(request):
        return redirect(disallowed_url)
    if form_class is None:
        form_class = backend.get_form_class(request)

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_user = backend.register(request, **form.cleaned_data)
            if success_url is None:
                to, args, kwargs = backend.post_registration_redirect(request, new_user)
                return redirect(to, *args, **kwargs)
            else:
                return redirect(success_url)
    else:
        form = form_class()

    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(template_name,
                              {'form': form},
                              context_instance=context)

@login_required
def profile(request,template_name='accounts/user_profile.html'):

    if request.user.is_authenticated():
        print request.user.get_profile().activation_key

    
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            sex = form.cleaned_data['sex']
            description = form.cleaned_data['description']
            profile = request.user.get_profile()
            if 'photos' in request.FILES:
                profile.photos = request.FILES["photos"]
                profile.sex = form.cleaned_data['sex']
                profile.description = form.cleaned_data['description']

            if sex in SEX_CHOICES:
                profile.sex = sex;
            
            if description !=None and description !="":
                profile.description = description;

            profile.save()
        else:
            form = UserProfile()
    else:
        form = UserProfile()

    return render_to_response(template_name,{'form': form},context_instance=RequestContext(request))