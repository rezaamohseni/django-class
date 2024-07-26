from django.shortcuts import render , redirect
from .forms import LoginForm , RegisterForm , ChangePasswordForm
from django.contrib.auth import login , logout , authenticate , password_validation
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages



def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form' : form,
        }
        return render(request , 'registrations/login.html' , context=context)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
    if user is not None:
        login(request , user)
        return redirect('/')
    else:
        messages.add_message(request ,messages.ERROR,'input data is not valid')
        return redirect('accounts:login')

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')

def signup_user(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user )
            messages.add_message(request , messages.SUCCESS , 'your account was created successfuly')
            return redirect('/')
        else:
            messages.add_message(request , messages.ERROR, 'your data is not valid')
            return redirect('accounts:signup')

    else:
        form = RegisterForm()
        context = {
            'form' : form
            }
        return render(request , 'registrations/signup.html' , context=context)

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                old_password = request.POST.get('old_password')
                pass1 = request.POST.get('new_password1')
                pass2 = request.POST.get('new_password2')
                user = request.user
                if user.check_password(old_password):
                    if (pass1 == pass2) and (pass1 and pass2) and (pass1!=old_password):
                        user.set_password(pass1)
                        try:
                            password_validation.validate_password(pass1)
                            user.set_password(pass1)
                            user.save()
                            login((request , user))
                            messages.add_message(request , messages.SUCCESS , 'your password was changed successfuly')
                            return redirect('/')
                        except:
                                messages.add_message(request , messages.ERROR, 'your new password is not valid')
                                return redirect('accounts:change_password')
                    else:
                        messages.add_message(request , messages.ERROR, 'your new password are not same ')
                        return redirect('accounts:change_password')
                else:
                    messages.add_message(request , messages.ERROR, 'your old password  is not valid')
                    return redirect('accounts:change_password')

                                                           
        else:
            form = ChangePasswordForm()
            context = {
                'form' : form,
            }
            return render(request , 'registrations/change_password.html' , context=context)
    else:
        messages.add_message(request ,messages.ERROR,'input data is not valid')
        return redirect('accounts:login')
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
