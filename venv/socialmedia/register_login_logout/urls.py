from django.urls import path
from register_login_logout import views

app_name = 'register_login_logout'

urlpatterns = [
    path('', views.register, name='register'),
]