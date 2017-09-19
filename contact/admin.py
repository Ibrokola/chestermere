from django.contrib import admin

from .models import ContactHeader, Contact


admin.site.register(ContactHeader)
admin.site.register(Contact)