from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse

from django.db.models import Q


from .models import ImageHeader, Service




def service_list(request):
    index_page = ImageHeader.objects.all()
    service1 = Service.objects.filter(parts__title='part1')
    service2 = Service.objects.filter(parts__title='part2')
    # service = Service.objects.all()
    template = 'services/list_view.html'
    context ={
        "index_page": index_page,
        # "service": service,
        "service1": service1,
        "service2": service2
    }
    return render(request, template, context)


def service_detail(request, slug=None):
    # service1 = Service.objects.all()
    service1 = Service.objects.filter(parts__title='part1')
    service2 = Service.objects.filter(parts__title='part2')
    try:
        service = get_object_or_404(Service, slug=slug)
    except Service.MultipleObjectsReturned:
        service = Service.objects.filter(slug=slug).order_by('title').first()

    template = 'services/detail_view.html'
    context ={
        "service1": service1,
        "service2": service2,
        "service": service
    }
    return render(request, template, context)