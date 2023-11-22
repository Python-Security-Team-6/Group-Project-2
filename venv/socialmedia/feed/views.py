from django.shortcuts import render
from .models import Post

# Create your views here.
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'feed.html', {'posts': posts})

