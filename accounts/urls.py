from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
import views

urlpatterns=patterns('',
		url(r'^signup/$', views.register),
		url(r'^login/$', login),
		url(r'^logout/$', logout),
		url(r'^welcome/$', views.welcome),
		)
