from django.urls import path
from views import profilepage

urlpatterns = [
    path("", profilepage, name="profilepage"),
]