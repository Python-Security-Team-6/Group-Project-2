from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment, Share
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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



@login_required
def share_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    Share.objects.create(user=request.user, post=post)
    post.shared_count += 1
    post.save()

    return JsonResponse({'shares': post.shared_count})
"""
@login_required
def get_comments(request):
    post_id = request.GET.get('post_id')
    post = get_object_or_404(Post, post_id=post_id)
    comments = post.comments.all()
    context = {'comments': comments}
    return render(request, 'feed/comments.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    
    # Check if the user has already liked the post
    if request.user in post.likes.all():
        # User has already liked, so unlike
        post.likes.remove(request.user)
        liked = False
    else:
        # User hasn't liked, so like
        Like.objects.create(user=request.user, post=post)
        liked = True
    
    # Update the likes count
    likes_count = post.likes.count()

    # Return JSON response
    return JsonResponse({'liked': liked, 'likes_count': likes_count})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    text = request.POST.get('comment_text')
    if text:
        Comment.objects.create(user=request.user, post=post, text=text)
    return redirect('feed')

@login_required
def share_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    post.shared_count += 1
    post.save()
    return redirect('feed')

"""