from django.conf.urls import url

from . import views

app_name = 'merger'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^resolve/(?P<merge_id>[0-9]+)$', views.resolve, name='resolve'),
	url(r'^(?P<merge_id>[0-9]+)/$', views.merge, name='merge'),
]