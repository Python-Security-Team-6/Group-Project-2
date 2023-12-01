# userprofile/urls.py

from django.urls import path
from .views import about_me, user_profile_view

app_name = 'user_profile'

urlpatterns = [
    path('user_profile/<str:username>/', user_profile_view, name='user_profile'),
    path('<str:username>/about_me/', about_me, name='about_me'),
    
  
]
