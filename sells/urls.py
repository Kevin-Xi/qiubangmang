'''Url request dispatcher'''

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
		url(r'^post/$', views.post),
		(r'^(\d{1,})/$', views.show_ability),
		)
