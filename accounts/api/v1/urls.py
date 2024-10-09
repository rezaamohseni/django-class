from django.urls import path
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "account-api"

urlpatterns = [
    path("registration/", RegisterationView.as_view(), name="registration"),
    # path('token/login' , CustomObtainAuthToken.as_view() , name='login'),
    path("token/logout", DeleteTokenView.as_view(), name="logout"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("change_password", ChangepasswordView.as_view(), name="change_password"),
]
