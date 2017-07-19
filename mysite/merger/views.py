# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Merge

def index(request):
	latest_merge_list = Merge.objects.order_by('-raised_on')[:2]
	# print(latest_merges_list)
	# template = loader.get_template('merger/index.html')
	context = {
		'latest_merge_list': latest_merge_list,
	}
	# return HttpResponse(template.render(context, request))
	return render(request, 'merger/index.html', context) # using render() shortcut

   

def merge(request, merge_id):
	# try:
	# 	merge = Merge.objects.get(pk=merge_id)
	# except Merge.DoesNotExist:
	# 	raise Http404("Merge does not exist")
	merge = get_object_or_404(Merge, pk=merge_id)
	context = {'merge':merge}
	return render(request, "merger/merge.html", context)
	# return HttpResponse("this page belongs to merge: %s" % merge_id)

def resolve(request, merge_id):
	return HttpResponse("%s resolved" % merge_id)