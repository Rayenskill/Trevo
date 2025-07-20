from django.urls import path
from . import views

# urlpatterns of the app checks the function names defined in views
urlpatterns = [
    path("login_user", views.login_user, name="login"),
]

