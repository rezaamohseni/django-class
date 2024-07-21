from django.shortcuts import render
from django.shortcuts import render
from services.models import SpecialService
from .models import FrequentlyQuestions , ContactUs
from services.models import Team

def home(request):

    context = {
        'specials': SpecialService.objects.filter(status=True),
        'team' : Team.objects.filter(status=True),
        'questions': FrequentlyQuestions.objects.filter(status=True)[::-1],
        }
    
    return render(request, 'root/index.html', context=context)


def contact(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    subject = request.GET.get('subject')
    message = request.GET.get('message')
    return render(request, "root/contact.html")


def about(request):
    context = {
        'team' : Team.objects.filter(status=True),
        }
    return render(request, "root/about.html", context=context)

