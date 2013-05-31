from django.conf.urls import patterns, url
#from django.contrib.auth.views import login, logout
import views

urlpatterns=patterns('',
		url(r'^signup/$', views.register),
		url(r'^login/$', views.login),
		url(r'^logout/$', views.logout),
		url(r'^welcome/$', views.welcome),
		url(r'^(\d{1,})/$', views.homepage),
		)
