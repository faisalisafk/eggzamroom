import requests
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

from django.apps import apps
from accounts.models import User, Teacher
from .models import Course, Exam
from .forms import CourseForm, ExamForm


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            if request.method == 'POST':
                form = CourseForm(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    subject = form.cleaned_data['subject']
                    teacher = Teacher.objects.get(pk=request.user.pk)
                    c = Course(title=title, subject=subject, teacher=teacher)
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
                           'form': form}
                return render(request, 'teacher/teacher_courses.html', context)
        else:
            return redirect('/logout/')
    else:
        return redirect('/login/')


def coursePage(request, coursePk):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            course = Course.objects.get(pk=coursePk)
            exam = Exam(title=title, description=description, course=course)
            exam.save()
            return HttpResponseRedirect(request.path_info)
        else:
            return HttpResponse("<h1>Invalid form</h1>")

    else:
        form = ExamForm()
        exams = Exam.objects.filter(course=coursePk)
        context = {'exams': exams,
                   'form': form}
        return render(request, 'teacher/exams.html', context)
