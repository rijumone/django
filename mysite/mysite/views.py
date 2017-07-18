from django.http import Http404,HttpResponse
# from django.template import Template,Context
# from django.template.loader import get_template
from django.shortcuts import render

import datetime

def hello(request):
	return HttpResponse("Ki re?!")

def current_datetime(request):
	now = datetime.datetime.now()
	
	# t = Template("It is now {{ now }}.")
	# t = get_template('current_datetime.html')
	# html = t.render({'now':now})
	# return HttpResponse(html)
	return render(request, 'current_datetime.html', {'now':now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "in " + str(offset) + " hours, it will be " + str(now)
	return HttpResponse(html)