from django.urls import path
from django.shortcuts import redirect
from . import views

# urlpatterns of the app checks the function names defined in views
urlpatterns = [
    path('', lambda request: redirect('login', permanent=True)),
    path("login/", views.login_user, name="login"),
]

