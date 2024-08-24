from rest_framework import serializers
from ...models import CustomUser
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('email' , 'password' , 'password1')

    def validate(self, attrs):
        pass1 = attrs['password']
        pass2 = attrs['password1']
        if pass1 != pass2:
            raise serializers.ValidationError({
                'detail' : 'Passwords must match'
                })
        
        try:
            validate_password(pass1)

        except ValidationError as e:
            raise serializers.ValidationError({
                'detail' : list(e.messages)
                })
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1')
        return CustomUser.objects.create_user(**validated_data)
    


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs







