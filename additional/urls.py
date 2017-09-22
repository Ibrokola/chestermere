from django.conf.urls import url
from django.contrib import admin

from .views import extra_detail

urlpatterns = [
    url(r'^$', extra_detail, name='extra_detail')
]