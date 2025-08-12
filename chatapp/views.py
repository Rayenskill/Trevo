from django.shortcuts import render
# Create your views here.

def index_connected(request, room_name):
    return render(request, "index.html", {'room_name': room_name})


def index(request):
    return render(request, "index.html")


