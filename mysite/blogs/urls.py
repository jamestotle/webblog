from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogs import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.test, name = 'page'),
    url(r'^(?P<page_index>\d+)/$', views.page, name='page'),
    url(r'^tag/(?P<tag_name>[^/]+)/(?P<page_index>\d+)/$', views.tagShow, name='tag'),
    url(r'^tag/(?P<tag_name>[^/]+)/$', views.tagShow, name='tag'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),

    # url(r'^()', include('polls.urls')),
)
