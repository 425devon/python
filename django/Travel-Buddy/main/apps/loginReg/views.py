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
        curUser = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = curUser.id
        request.session['name'] = curUser.first_name 
    return redirect('/travels')

def login(request):
    if len(User.objects.filter(email = request.POST['email'])) == 1:
        curUser = User.objects.get(email = request.POST['email'])
        curPass = bcrypt.checkpw(request.POST['password'].encode(), curUser.password.encode())
        if curPass == True:
            request.session['user_id'] = curUser.id 
            request.session['name'] = curUser.first_name 
            return redirect('/travels')
        else:
            messages.add_message(request, messages.WARNING, 'Incorrect password!')
    else:
        messages.add_message(request, messages.WARNING, 'User not found, need to register?')
    

    return redirect('/')
