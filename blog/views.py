from django.shortcuts import render
from django.http import HttpResponse

from .models import Posteo

def index(request):
    return render(request, 'blog/index.html')


def post(request):
    latest_post_list = Posteo.objects.all
    return render(request, "blog/post.html", {
        'latest_post_list': latest_post_list
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