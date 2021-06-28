from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),

]