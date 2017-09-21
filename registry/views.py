from django.shortcuts import render

import os

from mimetypes import guess_type

from django.conf import settings
from django.utils.encoding import force_bytes
from wsgiref.util import FileWrapper
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import RegHeaderImage, Section, RegForm



def reg_list(request):
    # header = RegHeaderImage.objects.all()
    # template = 'registry/regforms.html'
    # context = {
    #     'header': header
    # }
    # return render(request, template, context)
    pass

def reg_detail(request):
    header = RegHeaderImage.objects.all()
    reg1 = RegForm.objects.filter(section__title='section1')
    reg2 = RegForm.objects.filter(section__title='section2')
    template = 'registry/regforms.html'
    context = {
        'header': header,
        'reg1': reg1,
        'reg2': reg2
    }
    return render(request, template, context)

def reg_download(request):
    pass