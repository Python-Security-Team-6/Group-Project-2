from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment, Share
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.cache import never_cache


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
    post = get_object_or_404(Post, post_id=post_id, user=request.user)

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
    post = get_object_or_404(Post, post_id=post_id, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('feed')

    return render(request, 'delete_post.html', {'post': post})
    
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()

    return JsonResponse({'likes': post.like_set.count(), 'liked': created})


@login_required
def comment_post(request, post_id):
    post = Post.objects.get(post_id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            comment = Comment.objects.create(user=request.user, post=post, content=content)
            return JsonResponse({'username': comment.user.username, 'content': comment.content})
        else:
            return JsonResponse({'error': 'Content cannot be empty.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


@never_cache
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Delete the comment
    comment.delete()

    # Send a response with status 204 (No Content)
    return HttpResponse(status=204)



@login_required
def share_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    Share.objects.create(user=request.user, post=post)
    post.shared_count += 1
    post.save()

    return JsonResponse({'shares': post.shared_count})
