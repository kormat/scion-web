from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_scion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lambda _: HttpResponseRedirect('ad_manager/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ad_manager/', include('ad_manager.urls')),
)
