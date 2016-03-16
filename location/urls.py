from django.conf.urls import include, url
from django.contrib import admin

from location import urls as location_urls


urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^location/', include(location_urls), name='location'),
        url(r'^$', views.index, name='index'),
]
