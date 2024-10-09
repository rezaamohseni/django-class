from django import forms
from .models import ContactUs


class ContactUSForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ("name", "email", "subject", "message")
