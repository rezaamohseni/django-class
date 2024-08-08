from rest_framework import serializers
from services.models import Service




class Serviceserializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['name','content' , 'title' , 'description' , 'price']