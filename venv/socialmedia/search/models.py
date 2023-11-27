from django.db import models
from feed.models import Post
from django.contrib.auth.models import User

# Create your models here.

class SearchResult(models.Model):
    user_result = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_result = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Search Result - {self.user_result.username if self.user_result else ''} / {self.post_result.content if self.post_result else ''}"