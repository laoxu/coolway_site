# -*- encoding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

def user_page(request):
    name = "程东"
    return render_to_response('users/home_page.html', {'user_name': name})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours(s), it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)

def login():
    pass

def logout():
    pass

def hello(request):
    return HttpResponse("hello world")
