from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('course/<int:coursePk>/', views.coursePage, name='coursePage'),
    path('exam/<int:examPk>/', views.formPage, name='formPage'),
    path('exam/<int:examPk>/saveFormTitle', views.saveFormTitle, name='saveFormTitle'),
    path('exam/<int:examPk>/saveFormDes', views.saveFormDes, name='saveFormDes'),
    path('exam/<int:examPk>/saveQuestion', views.saveQuestion, name='saveQuestion'),
    path('exam/<int:examPk>/saveMark', views.saveMark, name='saveMark'),
    path('exam/<int:examPk>/editOption', views.editOption, name='editOption'),
    path('exam/<int:examPk>/deleteOption', views.deleteOption, name='deleteOption'),
    path('exam/<int:examPk>/addOption', views.addOption, name='addOption'),
    path('exam/<int:examPk>/addQuestion', views.addQuestion, name='addQuestion'),
    path('exam/<int:examPk>/delQuestion', views.delQuestion, name='delQuestion'),
    path('<int:formPk>/toggle',views.toggleForm, name='toggleForm'),
    path('<int:examPk>/viewScore',views.viewScore, name='viewScore'),
    path('deletecourse/<int:coursePk>/', views.deletecourse, name='deletecourse'),
    path('deleteexam/<int:examPk>/', views.deleteexam, name='deleteexam'),
    path('editCourse/<int:coursePk>/', views.editCourse, name='editCourse'),
]
