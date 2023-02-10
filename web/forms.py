from django import forms
from django.forms import models

from web.models import Account


class LoginForm(models.ModelForm):
    class Meta:
        model = Account
        fields = ['email','password']

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type":"email",
        "class":"form-control"
    }),label="Domain\\user name")

    password = forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        "class": "form-control"
    }), label="Password")
