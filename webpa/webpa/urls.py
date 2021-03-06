from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webpa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls.py.py')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pc/', include('pachong.urls')),
    url(r'^mg/', include('mg.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'mg/logo.html'}),
)
