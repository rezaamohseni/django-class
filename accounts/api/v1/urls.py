from django.urls import path
from .views import *

app_name = 'account-api'

urlpatterns = [
    path('registration/' , RegisterationView.as_view() , name='registration')
]
