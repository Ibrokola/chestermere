from django.contrib import admin

from .models import Service, ImageHeader, Part

admin.site.register(Part)
admin.site.register(Service)
admin.site.register(ImageHeader)