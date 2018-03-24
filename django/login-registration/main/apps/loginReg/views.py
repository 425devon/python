from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt



def index(request):
    return render(request, 'loginReg/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        return render(request, 'loginReg/index.html', {"errors": User.objects.basic_validator(request.POST)})

    else:
        User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        messages.add_message(request, messages.SUCCESS, 'Successfully registered!')
    return render(request, 'loginReg/success.html')

def login(request):
    if len(User.objects.filter(email = request.POST['email'])) == 1:
        curUser = User.objects.get(email = request.POST['email'])
        curPass = bcrypt.checkpw(request.POST['password'].encode(), curUser.password.encode())
        if curPass == True:
            messages.add_message(request, messages.SUCCESS, 'Successfully logged in!')
            return render(request, 'loginReg/success.html')
        else:
            messages.add_message(request, messages.WARNING, 'Incorrect password!')
    else:
        messages.add_message(request, messages.WARNING, 'User not found, need to register?')
    

    return redirect('/')
