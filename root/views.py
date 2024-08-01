from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render , redirect
from services.models import SpecialService
from .models import FrequentlyQuestions , ContactUs
from services.models import Team
from .forms   import ContactUSForm
from django.contrib import messages
from django.views.generic import TemplateView

# def home(request):

#     context = {
#         'specials': SpecialService.objects.filter(status=True),
#         'team' : Team.objects.filter(status=True),
#         'questions': FrequentlyQuestions.objects.filter(status=True)[::-1],
#         }
    
#     return render(request, 'root/index.html', context=context)

class HomeView(TemplateView):
    template_name = 'root/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['team'] = Team.objects.all()
        context ['questions'] = FrequentlyQuestions.objects.all()
        context ['specials'] = SpecialService.objects.all()
        return context 


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

# def about(request):
#     context = {
#         'team' : Team.objects.filter(status=True),
#         }
#     return render(request, "root/about.html", context=context)
class AboutView(TemplateView):
    template_name = "root/about.html"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context ['team'] = Team.objects.all()
        return context 
        