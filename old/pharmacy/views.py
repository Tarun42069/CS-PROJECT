from django.shortcuts import render
from cgitb import html

# Create your views here.
def home(request):
    return render(request,'homepage.html')
