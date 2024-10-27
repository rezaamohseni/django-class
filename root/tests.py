from django.test import TestCase
from django.urls import reverse , resolve
from .forms import ContactUSForm
from services.forms import CommentForm
from accounts.models import CustomUser
from .views import (HomeView,
                    AboutView,
                    contact) 
#test for url 
class TestUrl(TestCase):
    def setUp(self):
        self.user = user = CustomUser.objects.create_user(email="user@example.com" , password="Hamidrez@62" )

    def test_url_home(self):
        url = reverse("root:home")
        self.assertEqual(resolve(url).func.view_class , HomeView)

    def test_url_contact(self):
        url = reverse("root:contact")
        self.assertEqual(resolve(url).func , contact)
#test form
    def test_form_true_contact(self):
        form = ContactUSForm(data={
            "name": "reza",
            "email" : "admin@test.com",
            "subject" : "text",
            "message" : "text"
        })
        self.assertTrue(form.is_valid())
    def test_form_false_contact(self):
        form = ContactUSForm(data={
            "name": "reza",
            "email" : "1",
            "subject" : "text",
            "message" : "text"
        })
        self.assertFalse(form.is_valid())
#test form many to many fields
    def test_form_comment(self):
        form = CommentForm(data={
            "user": self.user,
            "product_name" : "admin@gmail.com",
            "message" : "text"
        })
        self.assertTrue(form.is_valid())