from multiprocessing import context
from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def areachart(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'area.html', context)


def barchart(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'bar.html', context)


def bubblechart(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'bubble.html', context)


def dpchart(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'dp.html', context)


def piechart(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'pie.html', context)


def columnchart(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'column.html', context)

    
def polarchart(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'polar.html', context)


def radarchart(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'radar.html', context)