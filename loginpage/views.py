from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # built-in contrib.auth
        if user is not None:
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    else:
        return render(request, "login.html", {})
    
# commit