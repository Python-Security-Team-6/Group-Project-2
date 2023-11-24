from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(user=request.user, content=content)
    return redirect('home')  

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    Like.objects.create(user=request.user, post=post)
    return redirect('home')  

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    text = request.POST.get('comment_text')
    if text:
        Comment.objects.create(user=request.user, post=post, text=text)
    return redirect('home')  

def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.shared_count += 1
    post.save()
    return redirect('post_detail', post_id=post_id)

@login_required
def some_view(request):
    posts = Post.objects.all()
    return redirect('testing_posts')

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'posts/post_detail.html', context)