import requests
from django.shortcuts import render,redirect

from django.apps import apps
from accounts.models import User,Teacher
from .models import Course
from .forms import CourseForm

def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CourseForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                subject = form.cleaned_data['subject']
                teacher = Teacher.objects.get(pk = request.user.pk)
                c = Course(title=title,subject=subject,teacher=teacher)
                c.save()
                return redirect('/teacher/')

        else:
            form = CourseForm()
            userDetails = User.objects.get(pk=request.user.pk)
            courseList = Course.objects.filter(teacher=request.user.pk)
            context = {'user': userDetails,
                       'course': courseList,
                       'form': form }
            return render(request, 'teacher/teacher_courses.html', context)

def addCourse(request):
    pass