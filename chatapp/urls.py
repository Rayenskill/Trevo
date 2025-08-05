from django.urls import path, include
from . import views


# While in example.com/chat/

urlpatterns = [
    path("", views.index, name="index"),
]
