# #userprofile forms.py

from django import forms
from .models import UserProfile

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about_me']

