from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from home.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about/', include('about.urls')),
    url(r'^forms/', include('registry.urls', namespace='reg')),
    url(r'^calendar/', include('additional.urls')),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^services/', include('services.urls', namespace='services')),
    url(r'^certificates/', include('certificates.urls', namespace='cert')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)