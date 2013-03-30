from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from views import index
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qiubangmang.views.home', name='home'),
    # url(r'^qiubangmang/', include('qiubangmang.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	('^$', index),
	(r'^site_medias/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS,'show_indexes':True}),
	(r'^accounts/login/$',login),
	(r'^accounts/logout/$',logout),
	url(r'^accounts/', include('accounts.urls')),
)
