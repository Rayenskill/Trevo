from django.urls import path
from views import listing

urlpatterns = [
    path("", listing, name=listing),
]