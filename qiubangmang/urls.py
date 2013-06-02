from django.conf.urls import patterns, include, url
from views import index
import settings

# enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	('^$', index),
	# static dir
	(r'^site_medias/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS,'show_indexes':True}),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^tasks/', include('tasks.urls')),
	url(r'^sells/', include('sells.urls')),
)
