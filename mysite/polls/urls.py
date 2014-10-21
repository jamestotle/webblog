from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index,name='index'),
    url(r'^(?P<poll_id>\d)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d)/result/$', views.result, name='result'),
    url(r'^(?P<poll_id>\d)/vote/$', views.vote, name='vote'),
)