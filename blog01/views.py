from django.shortcuts import render, get_object_or_404
from .models import Blog

def index(request):
    posts = Blog.objects.order_by('-published')
    return render(request, '../templates/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, '../templates/post_detail.html', {'post': post})

# Create your views here.
