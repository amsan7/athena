from django.conf.urls import patterns, include, url
from django.contrib import admin
from users import views

urlpatterns = patterns('',
	url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^groups/', include('groups.urls', namespace="groups")),
    url(r'^users/', include('users.urls', namespace="users"))
)
