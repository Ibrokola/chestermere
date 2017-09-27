from django.conf.urls import url
from django.contrib import admin

from .views import reg_detail, reg_list

urlpatterns = [
    url(r'^$', reg_list, name='reg_list'),
    url(r'^(?P<cat_slug>[\w-]+)/$', reg_detail, name='form_detail'),
]