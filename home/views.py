from django.shortcuts import render


from .models import HomeCarousel, Marketing, HomeIntro, Reminder

def home(request):
    carousel = HomeCarousel.objects.all()
    market = Marketing.objects.all()
    intro = HomeIntro.objects.all()
    remind = Reminder.objects.all()
    context = {
        "carousel": carousel,
        "market": market,
        "intro": intro,
        "remind":remind,
    }
    template = "home/home.html"
    return render(request, template, context)