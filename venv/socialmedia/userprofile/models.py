# userprofile/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    cover_pic = models.ImageField(upload_to='cover_pics', blank=True)
    about_me = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

