from django.shortcuts import render , redirect
from services.models import SpecialService
from .models import FrequentlyQuestions , ContactUs
from services.models import Team
from .forms   import ContactUSForm

def home(request):

    context = {
        'specials': SpecialService.objects.filter(status=True),
        'team' : Team.objects.filter(status=True),
        'questions': FrequentlyQuestions.objects.filter(status=True)[::-1],
        }
    
    return render(request, 'root/index.html', context=context)

def contact(request):
    if request.method == 'POST':
        form = ContactUSForm(request.POST)
        if form.is_valid():
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        # new_contact = ContactUs()
        # new_contact.name = name
        # new_contact.email = email
        # new_contact.subject = subject
        # new_contact.message = message
        # new_contact.save()
        return render(request, "root/contact.html")

    else:
        return render(request, "root/contact.html")


def about(request):
    context = {
        'team' : Team.objects.filter(status=True),
        }
    return render(request, "root/about.html", context=context)

