from django.shortcuts import render
from django.http import HttpResponse

from .models import Posteo

def index(request):
    posts = Posteo.objects.all()[:5]
    return render(request, 'blog/index.html',{
        'posts': posts
    })

def detail(request, slug_text):
    post = Posteo.objects.get(slug= slug_text)
    return render(request, 'blog/detail.html', {
        'post': post
    })

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, "blog/contact.html")

def photos(request):
    return render(request, "blog/photos.html")