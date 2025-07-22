from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('homepage.urls')),
    path("home/", include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name="logout"),
]

# commit