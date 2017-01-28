from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('vkapp.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'vkapp.utils.custom_404'
