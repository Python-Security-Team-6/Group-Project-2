# search/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from feed.models import Post
from .models import SearchResult
from django.db.models import Q

def search_results(request):
    query = request.GET.get('q', '')

    # Create search results for users
    user_results = User.objects.filter(username__icontains=query)

    # Create search results for posts
    post_results = Post.objects.filter(content__icontains=query)

    # Save search results to the database
    SearchResult.objects.filter(Q(user_result__isnull=False) | Q(post_result__isnull=False)).delete()
    SearchResult.objects.bulk_create([SearchResult(user_result=user) for user in user_results])
    SearchResult.objects.bulk_create([SearchResult(post_result=post) for post in post_results])

    # Retrieve search results from the database
    results = SearchResult.objects.filter(Q(user_result__isnull=False) | Q(post_result__isnull=False))

    return render(request, 'search/search_results.html', {'results': results, 'query': query})
