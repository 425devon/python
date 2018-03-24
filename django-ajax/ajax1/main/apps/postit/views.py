# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.core import serializers
from models import *

def post(request):
    
    return render(request, 'postit/post.html')

def create(request):
    Post.objects.create(desc = request.POST['note'])
    return render(request,'postit/allPost.html',{"posts": Post.objects.order_by("-id")})