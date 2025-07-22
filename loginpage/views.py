from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken.")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.is_active = True
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, "register.html", {})



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # built-in contrib.auth (admin panel)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    else:
        return render(request, "login.html", {})