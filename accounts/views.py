from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form' : form,
        }
        return render(request , 'lregistrations/l
                      
                      
                      
                      ogin.html' , context=context)
def logout_user(request):
    pass
def signup_user(request):
    pass
def change_password(request):
    pass
def reset_password(request):
    pass
def reset_password_done(request):
    pass
def reset_password_confirm(request):
    pass
def reset_password_complete(request):
    pass
def edit_profile(request):
    pass
