from django.conf.urls import patterns, url
import views

urlpatterns=patterns('',
		url(r'^post/$', views.post),
		(r'^post/(\d{1,})/$', views.showpost),
		)
