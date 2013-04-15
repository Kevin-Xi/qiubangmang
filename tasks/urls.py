from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
		url(r'^post/$', views.post),
		(r'^(\d{1,})/$', views.show_task),
		(r'^receive=(\d{1,})/$', views.receive),
		)
