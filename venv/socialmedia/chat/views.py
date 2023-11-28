from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

@login_required
def chat_room(request, user_id):
    # Retrieve chat messages between the logged-in user and the specified user
    chat_messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver_id=user_id)) |
        (models.Q(sender_id=user_id) & models.Q(receiver=request.user))
    ).order_by('timestamp')

    return render(request, 'chat/chat_room.html', {'chat_messages': chat_messages, 'user_id': user_id})
