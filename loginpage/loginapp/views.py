from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import logging

# Create your views here.
def login_user(request):
    logging.debug(f"Request method: {request.method}")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logging.debug(f"POST DATA: {request.POST}")
        user = authenticate(request, username=username, password=password) # built-in contrib.auth
        if user is not None:
            login(request, user)
            logging.debug("Code 0: User authenticated, redirecting to home")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            logging.debug("Code 1: Invalid credentials, setting error message")
            return redirect('login')
    else:
        logging.debug("Code 2: Rendering login page")
        return render(request, "registration/login.html", {})


    # if request.method == 'POST': # arriving on the page transporting info (after filling)(POST)
    #     username = request.POST['username']
    #     pass
    # else: # arriving on the page without transporting info (GET)
    #     return render(request, "registration/login.html", {})




