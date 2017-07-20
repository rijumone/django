from django.conf.urls import url

from . import views

app_name = 'merger'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.MergeView.as_view(), name='merge'),
	url(r'^resolve/(?P<merge_id>[0-9]+)$', views.resolve, name='resolve'),
]