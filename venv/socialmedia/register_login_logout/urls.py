from django.urls import path
from .views import register

app_name = 'register_login_logout'

urlpatterns = [
    path('register/', register, name='register'),
]