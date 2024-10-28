from django.test import TestCase
from django.urls import reverse , resolve
from .models import Comment
from accounts.models import CustomUser
from .views import (ServiceView,
                    Service_detailview,
                    ) 
#test for url and detail view for pk and str in url
class TestUrl(TestCase):
    def setUp(self):
        self.user =user = CustomUser.objects.create_user(email="user@example.com" , password="Hamidrez@62" )

    def test_url_services(self):
        url = reverse("services:services")
        self.assertEqual(resolve(url).func.view_class , ServiceView)

    def test_url_servicedetail(self):
        url = reverse("services:services-detail" , kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class , Service_detailview)

    def test_url_service_by_category(self):
        url = reverse("services:list_by_category" , kwargs={'category':"test"})
        self.assertEqual(resolve(url).func.view_class , ServiceView)
#test model > model user and create object in model
    def test_model_user(self):
        self.assertEqual(self.user.email , "user@example.com")
    def test_model_comment(self):
        comment = Comment.objects.create(user=self.user , product_name = "s1" , message="boos")
        self.assertEqual(comment.message , "boos")
#test exist object in model
    def test_model_comment(self):
        comment = Comment.objects.create(user=self.user , product_name = "s1" , message="boos")
        self.assertTrue(Comment.objects.filter(user=self.user).exists())
        