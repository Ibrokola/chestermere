from django.contrib import admin

from .models import Service, ImageHeader, Part

class ServiceInline(admin.TabularInline):
	model = Service

class ServiceAdmin(admin.ModelAdmin):
	list_filter = ['updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	list_display = ("__str__", 'updated', 'timestamp')
	fields = ['img', 'parts', 'title', 'slug', 'description', 'ext_link', 'ext_link2', 'ext_link3', 'ext_link4']
	search_fields = ['title']

	class Meta:
		model = Service


class PartAdmin(admin.ModelAdmin):
	inlines = [ServiceInline]
	class Meta:
		model = Part


admin.site.register(Part, PartAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ImageHeader)