from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login.html'),
    path('signup/', views.signup_view, name='signup.html'),
    path('home/', views.home_view, name='home.html'),
    ]