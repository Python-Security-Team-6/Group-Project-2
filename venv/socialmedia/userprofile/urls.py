# userprofile/urls.py

from django.urls import path
from .views import about_me, user_profile_view, change_cover_pic, change_profile_pic

app_name = 'user_profile'

urlpatterns = [
    path('user_profile/<str:username>/', user_profile_view, name='user_profile'),
    path('<str:username>/about_me/', about_me, name='about_me'),
    path('<str:username>/change-cover-pic/', change_cover_pic, name='change_cover_pic'),
    path('<str:username>/change-profile-pic/', change_profile_pic, name='change_profile_pic'),
  
]
