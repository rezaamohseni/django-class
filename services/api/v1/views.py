from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.models import Service
from .serializer import Serviceserializer



@api_view()
def services(request):
    services = Service.objects.all()
    serializer = Serviceserializer(services ,many = True)
    return Response(serializer.data)