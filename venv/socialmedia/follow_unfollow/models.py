from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
    
class Friend(models.Model):
    user = models.ForeignKey(User, related_name='user_friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend_users', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} follows {self.friend}'