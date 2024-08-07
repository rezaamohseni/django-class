from rest_framework import serializers
from services.models import Service



class Serviceserializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=220)

    class Meta:
        model = Service
        fields = '__all__'