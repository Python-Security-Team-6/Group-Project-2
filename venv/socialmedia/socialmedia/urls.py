from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
    path('chat/', include('chat.urls')),
    path('notifications/', include('notifications.urls')),
]
