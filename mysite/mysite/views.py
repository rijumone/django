from django.http import Http404,HttpResponse
import datetime

def hello(request):
	return HttpResponse("Ki re?!")

def current_datetime(request):
	now = datetime.datetime.now()
	html = str(now)
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "in " + str(offset) + " hours, it will be " + str(now)
	return HttpResponse(html)