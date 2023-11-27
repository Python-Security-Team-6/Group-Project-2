from django.urls import path
from .views import notification_list, not_logged_in_notifications_testing_view

urlpatterns = [
    path('list/', notification_list, name='notification_list'),
    path('not_logged_in_notifications_testing/', not_logged_in_notifications_testing_view, name='not_logged_in_notifications_testing'),
]
