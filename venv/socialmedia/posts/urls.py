"""
from django.urls import path
from .views import testingposts, post_detail, create_post, like_post, add_comment, share_post

urlpatterns = [
    path('testingposts/', testingposts, name='testingposts'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('create_post/', create_post, name='create_post'),
    path('posts/like_post/<int:post_id>/', like_post, name='like_post'),
    path('share_post/<int:post_id>/', share_post, name='share_post'),
]
"""