# blog/views.py

from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'blog_posts': blog_posts})
