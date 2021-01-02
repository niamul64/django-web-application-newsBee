from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth import authenticate, login
from accounts.models import ExtentionUser
from .forms import UserReg, ExtentUser
from .models import ExtentionUser
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
def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('signin')
    return redirect('signin')


def signup(request):
    e=''
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = ExtentUser(request.POST)

        if form1.is_valid() and form2.is_valid() and len(form1.cleaned_data['email'])>9 :
            userSaved=form1.save()


            ExtentionUser(author =userSaved, fullName=form2.cleaned_data['fullName'], country= form2.cleaned_data['country']).save()
            return redirect('signin')

        elif len(form1.cleaned_data['password1'])<8 :
            return render(request, 'signup.html', {'error': "password didn't matched or too short",'form1':form1,'form2':form2})
        else:
            return render(request, 'signup.html',{'error': "fill the form correctly", 'form1': form1, 'form2': form2})
    form1=UserReg()
    form2=ExtentUser()
    return render(request, 'signup.html', {'error':e , 'form1':form1,'form2':form2})