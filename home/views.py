from django.shortcuts import render


from .models import HomeCarousel, Marketing, HomeIntro

def home(request):
    carousel = HomeCarousel.objects.all()
    market = Marketing.objects.all()
    intro = HomeIntro.objects.all()
    context = {
        "carousel": carousel,
        "market": market,
        "intro": intro
    }
    template = "home/home.html"
    return render(request, template, context)