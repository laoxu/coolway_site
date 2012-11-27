# -*- encoding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import simplejson
from django.core.urlresolvers import reverse

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

    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            sex = form.cleaned_data['sex']
            description = form.cleaned_data['description']
            nickname = form.cleaned_data['nickname']
            profile = request.user.get_profile()
           

            if sex !=None and sex !="":
                profile.sex = sex
            
            if description !=None and description !="":
                profile.description = description

            if nickname !=None and nickname !='':
                profile.nickname = nickname

            profile.save()
        else:
            form = UserProfile()
    else:
        form = UserProfile()

    return render_to_response(template_name,{'form': form},context_instance=RequestContext(request))

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

@login_required
def uploadHeadImage(request):
    if request.method == 'POST':
        f = request.FILES.get('file')
        profile = request.user.get_profile()
        profile.photos = f
        profile.save()
        # 多了前缀/media
        fileurl = profile.headImage()
        print fileurl
        data = [{'name': fileurl, 'url':  fileurl, 'thumbnail_url':  fileurl, 'delete_url': fileurl, 'delete_type': "DELETE"}]
        response = JSONResponse(data, {}, response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
    
    else:
        response = JSONResponse([], {}, response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)