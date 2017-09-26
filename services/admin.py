from django.contrib import admin

from .models import Service, ImageHeader, Section

admin.site.register(Section)
admin.site.register(Service)
admin.site.register(ImageHeader)