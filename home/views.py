from django.shortcuts import render


from .models import HomeCarousel, Marketing

def home(request):
    carousel = HomeCarousel.objects.all()
    market = Marketing.objects.all()
    context = {
        "carousel": carousel,
        "market": market
    }
    template = "home/home.html"
    return render(request, template, context)