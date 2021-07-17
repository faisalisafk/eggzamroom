from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('course/<int:coursePk>/', views.coursePage, name='coursePage'),
    path('exam/<int:examPk>/',views.formPage,name='formPage'),
    path('exam/<int:examPk>/save',views.saveForm,name='save'),
]   