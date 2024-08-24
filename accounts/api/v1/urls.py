from django.urls import path
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'account-api'

urlpatterns = [
    path('registration/' , RegisterationView.as_view() , name='registration'),
    path('token/login' , CustomObtainAuthToken.as_view() , name='login'),
]
