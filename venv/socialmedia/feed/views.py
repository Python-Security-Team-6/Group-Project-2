from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('feed')

    return render(request, 'feed.html', {'posts': posts, 'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('feed')

    return render(request, 'delete_post.html', {'post': post})