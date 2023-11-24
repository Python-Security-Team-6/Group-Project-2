from django.contrib import admin
from django.urls import path, include
from posts.views import some_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testingposts/', some_view, name='some_view'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
]
