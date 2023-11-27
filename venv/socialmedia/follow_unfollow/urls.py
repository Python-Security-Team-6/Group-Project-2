from django.urls import path
from .views import home_view,friends_view,suggestions_view,your_friends_view,follow_user, unfollow_user,user_profile_view

urlpatterns = [
    path('', home_view, name='home'),
    path('friends/', friends_view, name='friends'), 
    path('suggestions/',suggestions_view,name='suggestions'),
    path('your-friends/', your_friends_view, name='your_friends'),
    path('follow-user/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow-user/<int:user_id>/', unfollow_user, name='unfollow_user'),
    path('user_profile/<str:username>/', user_profile_view, name='user_profile'),
    
    ]
    

   