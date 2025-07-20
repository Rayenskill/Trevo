from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST': # arriving on the page transporting info (after filling)(POST)
        pass
    else: # arriving on the page without transporting info (GET)
        return render(request, "registration/login.html", {})




