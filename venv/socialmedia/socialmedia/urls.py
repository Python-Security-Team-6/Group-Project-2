from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
    path('chat/', include('chat.urls')),
    path('notifications/', include('notifications.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='register_login_logout/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register_login_logout/logout.html'), name='logout'),
    path('', include('register_login_logout.urls')),
    path('', include('feed.urls')),
    path('search/', include('search.urls')),
    path('', include('follow_unfollow.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)