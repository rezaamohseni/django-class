from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from services.models import Service
from .serializer import Serviceserializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView




class ServiceApiView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self , request, *args, **kwargs):
        services = Service.objects.all()
        serializer = Serviceserializer(services ,many = True)
        return Response(serializer.data)


    def post(self , request, *args , **kwargs):
        if request.user.is_superuser:
            serializer = Serviceserializer(data=request.data )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_created)
        
            else:
                return Response(serializer.error)
        else:
            return Response('permission denied' , status=status.HTTP_401_UNAUTHORIZED)


class ServiceDetailApiview(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly] 

    def get(self , request, *args, **kwargs):
        id = kwargs.get('id')
        services = get_object_or_404(Service , id=id)
        serializer = Serviceserializer(services)
        return Response(serializer.data)
    def patch(self , request, *args, **kwargs):
        services = get_object_or_404(Service , id=id)
        serializer = Serviceserializer(services , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data ,status=status.HTTP_200_OK)

    
    def delete(self , request, *args, **kwargs):
        services = get_object_or_404(Service , id=id)
        services.delete()
        return Response('service deleted', status=status.HTTP_204_NO_CONTENT)






# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])  
# def services(request):
#     if request.method == 'GET':
#         services = Service.objects.all()
#         serializer = Serviceserializer(services ,many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         if request.user.is_superuser:
#             serializer = Serviceserializer(data=request.data )
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status=status.HTTP_201_created)
#             else:
#                 return Response(serializer.error)
#         else:
#             return Response('permission denied' , status=status.HTTP_401_UNAUTHORIZED)







# @api_view(['GET', 'PATCH','DELETE'])
# def services_detail(request , id):
#     service = get_object_or_404(Service,id=id)        
#     if request.method == 'GET':
#         # try:
#         #     services = Service.objects.get(id=id)
#         #     serializer = Serviceserializer(services)
#         #     return Response(serializer.data)
#         # except:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = Serviceserializer(service)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = Serviceserializer(service , data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data ,status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         service.delete()
#         return Response('service deleted', status=status.HTTP_204_NO_CONTENT)


