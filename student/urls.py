from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('course/<int:coursePk>/', views.coursePage, name='coursePage'),
    path('exam/<int:examPk>/', views.examFormPage, name='examFormPage'),
    path('exam/<int:examPk>/saveAnswer', views.saveAnswer, name='saveAnswer'),
    path('exam/<int:examPk>/detectionlog', views.WindowDetectionLog, name='detectionlog'),
    path('<int:formPk>/submit',views.submit,name='submit'),
]
