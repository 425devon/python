# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    
    return redirect('/blogs')

def blogs(request):
    response = "placeholder to displat a new list of blogs"
    return HttpResponse(response)

def new_blog(request):
    response = " placedholder to display a new form to create a blog"
    return HttpResponse(response)

def blog_num(request, number):
    response = 'placeholder to display blog '+str(number)
    return HttpResponse(response)

def blog_edit(request, number):
    response = 'placeholder to edit blog '+str(number)
    return HttpResponse(response)

def blog_delete(request, number):
    return redirect('/')

def create(request):
    print "*"*50
    return redirect("/blogs")
