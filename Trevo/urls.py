"""
URL configuration for Trevo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# The URLs from the start of navigation (i.e. when landing on the website.)
# path('' ...) are the paths of the website. Example : example.com/ for path('') or example.com/admin for path('admin')
# the include function allows to delegate the URL management to the separate apps. Example : include('homepage.urls') 
# allows the website (example.com/) to use the urls.py file of the app to know what to do.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('home/', include('homepage.urls')),
    path('authentication/', include('loginpage.urls')),
    path('chat/', include("chatapp.urls")),
    path("listing/", include("listing.urls")),
    path("profile/", include("profilepage.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)