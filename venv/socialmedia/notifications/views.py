from django.shortcuts import render, redirect
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def notification_list(request):
    # Check if the user is not logged in and the requested URL is /notifications/list/
    if not request.user.is_authenticated and request.path == '/notifications/list/':
        return redirect('not_logged_in_notifications_testing')

    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def not_logged_in_notifications_testing_view(request):
    return render(request, 'not_logged_in_notifications_testing.html')
