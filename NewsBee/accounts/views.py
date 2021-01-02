from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth import authenticate, login
from accounts.models import ExtentionUser
# Create your views here.

def signin(request):
    if request.method == 'POST':
        user =auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        print (request.POST['username'])
        if user is not None:
            auth.login(request, user)
            return redirect('signin')
        else:
            return render(request, 'signin.html',{'error':"incorrect user name or password"})

    return render(request, 'signin.html')