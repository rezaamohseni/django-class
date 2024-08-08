from django.urls import path 
from .views import *

app_name = 'services-api'

urlpatterns = [
    path('services' , ServiceApiView.as_view() , name='services'),
    path('services/<int:id>' , ServiceDetailApiview.as_view() , name='services_detail')
]
