from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('vkapp.urls')),
)

handler404 = 'vkapp.utils.custom_404'
