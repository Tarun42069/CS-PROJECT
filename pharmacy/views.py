from django.shortcuts import render
from cgitb import html
from cgitb import html
from http.client import HTTPResponse
from timeit import repeat
from unicodedata import name
from urllib import response
from webbrowser import get
from django.forms import PasswordInput
from django.shortcuts import render,redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect
from .models import Signup
from django.contrib.auth.models import User
from .forms import registration

# Create your views here.
def home(request):
    return render(request,'homepage.html')


def login_user (request): 
    submitted= False 
    log=0
    if request.method=="POST":    
        emai = request.POST['email']
        password = request.POST['password']
        User = authenticate(request, User_email=emai, password=password)
        if User is not None:
            log=1
            login(request, User)
            return redirect('/')
        else:
            messages.success(request,("There was an error"))
            return redirect('login.html')
        
    else:
        return render(request,'login.html')

def reg(request):
    if request.method=="POST":
        form=registration(request.POST)
        if form.is_valid:
            # form.save()
            first=request.POST['firstname']
            last=request.POST['lastname']
            emai=request.POST['email']
            pas1=request.POST['password1']
            pas2=request.POST['password2']
            # line1=request.POST['address1']
            # line2=request.POST['address2']
            # line3=request.POST['address3']
            regist=Signup(User_fname=first,User_lname=last,User_password=pas1,User_repaeat_password=pas2,
                        User_email=emai)
            if pas1==pas2:
                if  User.objects.filter(email=emai).exists():
                    messages.success(request,("The email already exists"))
                    return render(request,'reg.html')
                else:
                    # user=User.objects.create_user(username=name,email=emai,password=pas1,first_name=first,last_name=last)
                    Users = authenticate(request, User_email=emai, password=pas1)
                    
                    regist.save()
                    login(request,Users)  
                    return render(request,'login.html')
            else:
                messages.success(request,("The passwords do not match."))
                return render(request,'reg.html')
        else:
            return render(request,'reg.html')
        
    else:
        return render(request,'reg.html')

def genmed(request):
    return render(request,'generalmed.html')