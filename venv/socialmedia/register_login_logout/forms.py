from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input-group mb-3"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input-group mb-3"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-group mb-3"}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-group mb-3"}), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

