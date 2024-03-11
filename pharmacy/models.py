from django.db import models
from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Signup(models.Model):
    User_fname=models.CharField(max_length=200)
    User_lname=models.CharField(max_length=100)
    Phno=PhoneNumberField(blank=True)
    User_password=models.CharField(max_length=200)
    User_repaeat_password=models.CharField(max_length=200)
    User_email=models.EmailField(max_length=200)
    User_adl=models.CharField(max_length=100)
    User_adli=models.CharField(max_length=100)
    User_adlin=models.CharField(max_length=100)
