from django.shortcuts import render


from .models import HomeCarousel, Marketing, HomeIntro, Reminder

def home(request):
    carousel = HomeCarousel.objects.all()
    market = Marketing.objects.all().order_by('?')
    intro = HomeIntro.objects.all()
    remind = Reminder.objects.all().order_by('?')
    context = {
        "carousel": carousel,
        "market": market,
        "intro": intro,
        "remind":remind,
    }
    template = "home/home.html"
    return render(request, template, context)