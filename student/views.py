import requests
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

from django.apps import apps
from accounts.models import User, Student
from .models import Course
from .forms import CourseJoinForm


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            if request.method == 'POST':
                form = CourseJoinForm(request.POST)
                if form.is_valid():
                    courseCode = form.cleaned_data['courseCode']
                    course = Course.objects.get(courseCode=courseCode)
                    student = Student.objects.get(pk=request.user.pk)
                    c = JoinCourse(student=student)
                    c.save()
                    c.courses.add(course)
                    return redirect('/student/')
                else:
                    return HttpResponse("<h1>Invalid form</h1>")
            else:
                form = CourseJoinForm()
                userDetails = User.objects.get(pk=request.user.pk)
                courseList = Course.objects.filter(student=request.user.pk)
                context = {'user': userDetails,
                           'course': courseList,
                           'form': form}
                return render(request, 'student/student_courses.html', context)
        else:
            return redirect('/logout/')
    else:
        return redirect('/login/')


def coursePage(request, coursePk):

        form = ExamForm()
        exams = Exam.objects.filter(course=coursePk)
        context = {'exams': exams,
                   'form': form}
        return render(request, 'student/exams.html', context)

