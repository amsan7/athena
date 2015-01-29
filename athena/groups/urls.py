from django.conf.urls import patterns, url

from groups import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<group_id>\d+)/$', views.detail, name='detail'),
)
