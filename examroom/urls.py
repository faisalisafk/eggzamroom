"""examroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from accounts.views import home_view, login_view, signup_view, logout_view, teacher_signup_view
from teacher.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('teacher/', include('teacher.urls')),
    path('', home_view, name='accounts/home.html'),
    path('home', home_view, name='home'),
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
    path('signup_teacher', teacher_signup_view, name='signup_teacher'),
    path('logout/', logout_view, name='logout'),
]
