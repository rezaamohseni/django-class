from rest_framework.generics import GenericAPIView
from .serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status


class RegisterationView(GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self , request , *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
    
            
            return Response({
                'email' : serializer.validated_data['email'],

            })