from django.shortcuts import render

from .models import AddHeader, AddCategory



def extra_detail(request):
    header = AddHeader.objects.all()
    cat = AddCategory.objects.all()
    template = 'additional/extra.html'
    context = {
        'header': header,
        'cat': cat,
    }
    return render(request, template, context)