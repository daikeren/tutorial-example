from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^accounts/', include('allauth.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'trips.views.hello_world'),
    url(r'^$', 'trips.views.home'),
    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail',
        name='post_detail'),
)
