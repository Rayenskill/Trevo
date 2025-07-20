from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # built-in contrib.auth
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    else:
        return render(request, "registration/login.html", {})


    # if request.method == 'POST': # arriving on the page transporting info (after filling)(POST)
    #     username = request.POST['username']
    #     pass
    # else: # arriving on the page without transporting info (GET)
    #     return render(request, "registration/login.html", {})




