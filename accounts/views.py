from django.contrib.messages.api import error
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
import re

def signup(request):

    if request.method == "POST" and 'btnsignup' in request.POST:

        #Variables for fields

        first_name = None
        last_name  = None
        address    = None
        address2   = None
        city       = None
        state      = None
        zip_number = None
        email      = None
        username   = None
        password   = None
        terms      = None
        is_added   = None

        # Get values from the form 

        if 'first_name' in request.POST: first_name = request.POST['first_name']
        else: messages.error(request,'Error in first name')

        if 'last_name' in request.POST: last_name = request.POST['last_name']
        else: messages.error(request,'Error in last name')

        if 'address' in request.POST: address = request.POST['address']
        else: messages.error(request,'Error in address')

        if 'address2' in request.POST: address2 = request.POST['address2']
        else: messages.error(request,'Error in address2')

        if 'city' in request.POST: city = request.POST['city']
        else: messages.error(request,'Error in city')

        if 'state' in request.POST: state = request.POST['state']
        else: messages.error(request,'Error in state')

        if 'zip_number' in request.POST: zip_number = request.POST['zip_number']
        else: messages.error(request,'Error in zip')

        if 'username' in request.POST: username = request.POST['username']
        else: messages.error(request,'Error in username')

        if 'password' in request.POST: password = request.POST['password']
        else: messages.error(request,'Error in password')

        if 'terms' in request.POST: terms = request.POST['terms']
     
        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,'Error in email')

      

        if first_name and password and state and zip_number and email and username and last_name and city and address and address2:
          if terms == 'on':
            # check if  username taken
            if User.objects.filter(username = username).exists():
                messages.error(request , 'this username is taken')
            else: 
                # check if email taken
                if User.objects.filter(email = email).exists():
                    messages.error(request,'this email is taken')
                else: 
                    patt = '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                    if re.match(patt,email):
                        # add user
                        user = User.objects.create_user(
                        first_name=first_name, 
                        email=email, 
                        last_name=last_name, 
                        username=username, 
                        password=password )
                        user.save()
                        # add userprofile
                        userprofile = UserProfile(
                        user=user, 
                        address=address, 
                        address2=address2, 
                        zip_number=zip_number, 
                        state=state,
                        city=city )
                        userprofile.save()

                        first_name = " "
                        last_name  = " "
                        address    = " "
                        address2   = " "
                        city       = " "
                        state      = " "
                        zip_number = " "
                        email      = " "
                        username   = " "
                        password   = " "
                        terms      = None
                        messages.success(request,'You account is created')
                       
                        is_added = True
                    else:
                        messages.error(request , ' Invalid email ')

          else: messages.error(request , 'you must agree to the terms')


        else: messages.error(request,'check empty fields') 
            
     
        return render(request,'accounts/signup.html',{

            'first_name':first_name,
            'last_name':last_name,
            "username":username,
            'zip_number':zip_number,
            'city':city,
            'state':state,
            'address':address,
            'address2':address2,
            "password":password,
            'email':email,
            "is_added":is_added


        })

    else:
       return render(request,'accounts/signup.html')

def signin(request):

    if request.method == "POST" and 'btnlogin' in request.POST:

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            
        else: messages.error(request , 'Password or Username Invaild')
     
        return redirect('index')

    else:

       return render(request,'accounts/signin.html')

def profile(request):

    if request.method == "POST" and 'btnsave' in request.POST:
     
        return redirect('profile')

    else:
        return render(request,'accounts/profile.html')