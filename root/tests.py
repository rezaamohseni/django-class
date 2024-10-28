from django.test import TestCase , Client
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
#test response url for home
    def test_response_home(self):
        url = reverse("root:home")
        c = Client()
        response = c.get(path = url)
        self.assertEqual(response.status_code , 200)
#test exists form html
    def test_template_home(self):
        url = reverse("root:home")
        c = Client()
        response = c.get(url)
        self.assertTemplateUsed(response , template_name="root/index.html")        
    def test_template_content_home(self):
        url = reverse("root:home")
        c = Client()
        response = c.get(url)
        if "totam" not in str(response.content):
            raise AssertionError("content my be change") 
        # self.assertTrue(str(response.content).find("totam")) 
#test response status code in equal and not equal       
    def test_response_contac_200(self):
        url = reverse("root:contact")
        c = Client()
        c.force_login(self.user)
        response = c.get(url)
        self.assertEqual(response.status_code , 200)
    def test_response_contac_302(self):
        url = reverse("root:contact")
        c = Client()
        response = c.get(url)
        self.assertEqual(response.status_code , 302)