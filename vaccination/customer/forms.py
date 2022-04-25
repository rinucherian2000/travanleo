from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User





class UserRegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()