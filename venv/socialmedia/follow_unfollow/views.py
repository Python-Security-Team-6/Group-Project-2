# Function-Based View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Friend
from userprofile.models import UserProfile

from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.db.models import Q

def home_view(request):
    return render(request, 'home.html')

def friends_view(request):
    return render(request, 'friends.html')

@login_required
def suggestions_view(request):
    if request.method == 'POST':
        # Get the user_id from the POST data
        user_id_to_follow = request.POST.get('user_id')
        
        # Check if the user_id is valid
        if user_id_to_follow:
            # Get the user to follow
            user_to_follow = User.objects.get(pk=user_id_to_follow)
            
            # Create a Friend object
            Friend.objects.create(user=request.user, friend=user_to_follow)
            
            # Remove the friend from suggestions
            UserProfile.objects.filter(user=user_to_follow).delete()

    # Get the list of friends' user IDs
    friend_ids = Friend.objects.filter(user=request.user).values_list('friend', flat=True)

    # Exclude the current user and their friends from suggestions
    suggestion_list = UserProfile.objects.exclude(
        Q(user=request.user) | Q(user__in=friend_ids)
    )

    return render(request, 'suggestions.html', {'suggestion_list': suggestion_list})



@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(pk=user_id)
    Friend.objects.create(user=request.user, friend=user_to_follow)
    return redirect('suggestions')

@login_required
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(pk=user_id)
        friend_to_remove = Friend.objects.filter(user=request.user, friend=user_to_unfollow).first()

        if friend_to_remove:
            friend_to_remove.delete()
    except Friend.DoesNotExist:
        # Handle the case where the Friend object does not exist
        pass

    # Redirect to 'your_friends' with the updated friend list
    return redirect('your_friends')

@login_required
def your_friends_view(request):
    # Replace this with your logic to get the list of user's friends
    your_friends_list = Friend.objects.filter(user=request.user)
    return render(request, 'your_friends.html', {'your_friends_list': your_friends_list})

def user_profile_view(request, username):
    user = User.objects.get(username=username)
    # Your logic to render the user profile page
    return render(request, 'user_profile.html', {'user': user})
