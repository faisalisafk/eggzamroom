from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_student, name='dashboard_student'),

]