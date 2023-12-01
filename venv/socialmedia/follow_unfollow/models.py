from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class Friend(models.Model):
    user = models.ForeignKey(User, related_name='user_friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend_users', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} follows {self.friend}'