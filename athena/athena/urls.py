from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum import views

urlpatterns = patterns('',
	url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^groups/', include('groups.urls', namespace="groups")),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.user_profile, name='profile'),
)
