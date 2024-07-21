from django.shortcuts import render , redirect
from services.models import SpecialService
from .models import FrequentlyQuestions , ContactUs
from services.models import Team
from .forms   import ContactUSForm
from django.contrib import messages

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
            form.save()
        
            messages.add_message(request, messages.SUCCESS , 'your message was submited succsessfully')
            return render(request, "root/contact.html")
        
        else:
            messages.add_message(request, messages.ERROR , 'your input data may be incorrect')
            return render(request, "root/contact.html")


    else:
        form = ContactUSForm()
        return render(request, "root/contact.html" , context={'form' : form})

def about(request):
    context = {
        'team' : Team.objects.filter(status=True),
        }
    return render(request, "root/about.html", context=context)

