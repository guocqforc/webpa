# coding:utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^login/$', 'mg.views.login'),
    # (r'^about/$', 'mysite.views.about'),
    # (r'^rss/$', 'mysite.views.rss'),
)
