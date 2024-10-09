from rest_framework import serializers
from ...models import CustomUser
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core import exceptions
from rest_framework.authtoken.models import Token


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validate_dat = super().validate(attrs)
        validate_dat["user"] = self.user.id
        validate_dat["email"] = self.user.email
        return validate_dat


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ("email", "password", "password1")

    def validate(self, attrs):
        pass1 = attrs["password"]
        pass2 = attrs["password1"]
        if pass1 != pass2:
            raise serializers.ValidationError({"detail": "Passwords must match"})

        try:
            validate_password(pass1)

        except ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1")
        return CustomUser.objects.create_user(**validated_data)


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=("email"), write_only=True)
    password = serializers.CharField(
        label=("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=("Token"), read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_pass = serializers.CharField(max_length=30)
    new_pass1 = serializers.CharField(max_length=30)
    new_pass2 = serializers.CharField(max_length=30)

    def validate(self, attrs):
        pass1 = attrs.get("new_pass1")
        pass2 = attrs.get("new_pass2")
        if pass1 != pass2:
            msg = "pass 1 and pass2 must be the same"
            raise serializers.ValidationError(msg, code="authorization")

        return super().validate(attrs)

    def old_password_chek(self, attrs, request):
        old_pass = attrs.get("old_pass")
        pass1 = attrs.get("pass1")

        user = request.user
        if not user.check_password(old_pass):
            msg = "old pass doesnt match"
            raise serializers.ValidationError(msg, code="authorization")
        if old_pass == pass1:
            raise serializers.ValidationError(
                {"detail": "old password can not same as new password"}
            )

        return attrs

    def new_password_set(self, attrs, request):
        pass1 = attrs.get("new_pass1")
        user = request.user
        try:
            validate_password(pass1)

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})
        user.set_password(pass1)
        user.save()
        return attrs

    def delete_old_token_and_create_new(self, attrs, request):
        user = request.user
        user.auth_token.delete()
        token = Token.objects.create(user=user)
        return token
