from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):

   user         = models.OneToOneField(User , on_delete= models.CASCADE)

   address      = models.CharField(max_length=60)
   address2     = models.CharField(max_length=60)
   city         = models.CharField(max_length=60)
   state        = models.CharField(max_length=60)
   zip_number   = models.CharField(max_length=60)
  
   def __str__(self):
       return self.user.username
    
   


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    
    def __str__(self):
       return self.name
   