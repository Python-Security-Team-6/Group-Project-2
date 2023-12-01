
"""
from django.db import models
from django.contrib.auth.models import User
from feed.models import Post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        # Update the likes_count field in the associated post
        self.post.likes_count = self.post.likes.count()
        self.post.save()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(FeedPost, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

"""