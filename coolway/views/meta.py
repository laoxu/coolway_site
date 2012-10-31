from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from coolway.forms.qanda import CityForm
from coolway.models.city import City
import datetime


def new_city(request):
	if request.method =='POST':
		form = CityForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			now = datetime.datetime.now()
			city = City(name = data['name'],create_time=now,modify_time=now)
			city.save()
			return HttpResponseRedirect('../new_city')
		else:
			return render_to_response('new_city.html', {'form': form},context_instance=RequestContext(request))
	else:
		form = CityForm()
		return render_to_response('new_city.html', {'form': form},context_instance=RequestContext(request))