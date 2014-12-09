from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	# ex. /polls/meet
	url(r'^index/$',views.index , name="index"),
)
