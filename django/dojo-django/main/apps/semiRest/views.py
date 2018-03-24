# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from models import *

def index(request):
   
    return render(request,'semiRest/index.html', {"users": User.objects.all()} )

def newUser(request):

    return render(request,'semiRest/newUser.html')

def create(request):
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])

    return redirect('/rest')

def show(request, id):

    return render(request,'semiRest/showUser.html', {"users": User.objects.get(id = id)})

def edit(request, id):

    return render(request, 'semiRest/editUser.html',{"users": User.objects.get(id = id)})

def update(request, id):
    user = User.objects.get(id=id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()

    return redirect('/rest')

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()

    return redirect('/rest')


