from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def login(request):

    if 'email' not in request.session:
        return redirect('/auth/login/')

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=User.objects.get(email=email)
            if user.check_password(password):
                request.session['email']=user.email
                request.session['name']=user.name
                request.session['id']=user.id
                messages.success(request,"Login Successful")
                return redirect('/')

              
            else:
                return render(request,'login.html',{'error':'Invalid Password'})
            
        
        except User.DoesNotExist:
            return render(request,"login.html",{"error":"User Does not Exist"})