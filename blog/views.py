from django.shortcuts import render
from django.http import HttpResponse

from .models import Posteo

def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    latest_post_list = Posteo.objects.all
    return render(request, "blog/posts.html", {
        'latest_post_list': latest_post_list
    })

def detail(request, post_id):
    post = Posteo.objects.get(pk= post_id)
    return render(request, 'blog/detail.html', {
        'post': post
    })