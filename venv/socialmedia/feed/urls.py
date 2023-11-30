from django.urls import path
from .views import feed, edit_post, delete_post, like_post, comment_post, share_post



urlpatterns = [
    path('', feed, name='feed'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
    path('comment_post/<int:post_id>/', comment_post, name='comment_post'),
    path('share_post/<int:post_id>/', share_post, name='share_post'),
]
