# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.

def home(request):
    return render(request, 'home.html')

def registeruser(request):
    if request.method == 'POST':
        visible = False
        email = request.POST.get('email')
        Public_visibility = request.POST.get('Public_visibility')
        if Public_visibility == 'on':
            visible = True
        else:
            visible = False
        phone = request.POST.get('phone')
        birth_year = request.POST.get('birth_year')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1==password2:
            if CustomUser.objects.filter(email=email).exists():
                messages.info(request, "Email already taken!")
                return redirect('register')
            elif CustomUser.objects.filter(phone=phone).exists():
                messages.info(request, "Someone else already uses this phone number!")
                return redirect('register')
            else:
                user = CustomUser.objects.create_user(email=email, password=password1, Public_visibility=visible, phone=phone, birth_year=birth_year)
                user.save()
                return redirect('login')
        else:
            print("Passwords don't match")
            return redirect('register')
    return render(request, 'register.html')

def loginuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            messages.info(request, "Thank you!")
            login(request, user)
            return redirect('login')
        else:
            messages.info(request, "Please enter valid credentials!")
            return redirect('login')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')