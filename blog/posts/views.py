from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/index.html', {'posts':posts})

def show(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/show.html', {'post':post})
