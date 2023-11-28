from django.urls import path
from .views import feed, edit_post, delete_post

urlpatterns = [
    path('', feed, name='feed'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]
