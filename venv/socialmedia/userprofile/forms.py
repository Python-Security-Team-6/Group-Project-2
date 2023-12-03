# #userprofile forms.py

from django import forms
from .models import UserProfile

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about_me']

class ChangeCoverPicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['cover_pic']

class ChangeProfilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']
