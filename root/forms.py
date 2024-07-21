from django import forms

class ContactUSForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=220)
