from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse

from django.db.models import Q


from .models import ImageHeader, Service




def service_list(request):
    index_page = ImageHeader.objects.all()
    service = Service.objects.all()
    template = 'list_view.html'
    context ={
        "index_page": index_page,
        "service": service
    }
    return render(request, template, context)


def service_detail(request, slug=None):
    pass