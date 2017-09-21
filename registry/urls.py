from django.conf.urls import url
from django.contrib import admin

from .views import reg_detail

urlpatterns = [
    url(r'^$', reg_detail, name='form_detail')
]