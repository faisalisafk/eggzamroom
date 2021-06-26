import requests
from django.shortcuts import render,redirect,HttpResponse

from django.apps import apps
from accounts.models import User,Teacher
from .models import Course
from .forms import CourseForm

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
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
                    return HttpResponse("<h1>Invalid form</h1>")
            else:
                form = CourseForm()
                userDetails = User.objects.get(pk=request.user.pk)
                courseList = Course.objects.filter(teacher=request.user.pk)
                context = {'user': userDetails,
                           'course': courseList,
                           'form': form }
                return render(request, 'teacher/teacher_courses.html', context)
        else:
            return redirect('/logout/')
    else:
        return redirect('/login/')

