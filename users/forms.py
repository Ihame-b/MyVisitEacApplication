from dataclasses import field
from email.policy import default
# import email
# from pyexpat import model
# from unicodedata import name
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()
    name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email','phone', 'password1', 'password2']