from django.conf.urls import patterns, include, url
from rest_framework import routers
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from api import views

router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^zettaknight/api/', views.zettaknightview.as_view()),
    url(r'^zettaknight/user/share/(?P<username>.+)/$', views.zettaknightshareview.as_view()),
    url(r'^zettaknight/user/quota/(?P<username>.+)/$', views.zettaknightquotaview.as_view()),
    url(r'^zettaknight/group/quota/(?P<username>.+)/$', views.zettaknightquotaview.as_view())
)


