# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post
from markdown import markdown

# Create your views here
'''.
def index(request):
    # return HttpResponse("欢迎访问我的博客首页")
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页',
    })
'''
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html' ,context={
        'post_list':post_list,
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown(post.body)
    return render(request, 'blog/detail.html', context={'post': post})

