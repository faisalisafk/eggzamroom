from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('course/<int:coursePk>/', views.coursePage, name='coursePage'),
    path('exam/<int:examPk>/',views.formPage,name='formPage'),
    path('exam/<int:examPk>/saveForm',views.saveForm,name='saveForm'),
    path('exam/<int:examPk>/saveQuestion',views.saveQuestion,name='saveQuestion'),
    path('exam/<int:examPk>/editOption',views.editOption,name='editOption'),
]   