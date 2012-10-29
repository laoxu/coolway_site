from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

def index(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'current_date': now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours(s), it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("hello world")
