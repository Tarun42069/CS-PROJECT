from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import  Signup
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registration(ModelForm):
    class Meta:
        model=Signup
        fields=('User_fname','User_lname','User_email','Phno','User_password','User_repaeat_password','User_adl','User_adli','User_adlin')