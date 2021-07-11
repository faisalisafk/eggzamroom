import requests
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

from django.apps import apps
from accounts.models import User
from teacher.models import Course, Exam
from student.models import Student
from .forms import CourseJoinForm
from teacher.forms import ExamForm


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            if request.method == 'POST':
                form = CourseJoinForm(request.POST)
                if form.is_valid():
                    courseCode = form.cleaned_data['courseCode']
                    course = Course.objects.get(courseCode=courseCode)
                    student = Student.objects.get(pk=request.user.pk)
                    student.course.add(course)
                    return redirect('student/student_courses.html')
                else:
                    return HttpResponse("<h1>Invalid form</h1>")
            else:
                form = CourseJoinForm()
                userDetails = Student.objects.get(pk=request.user.pk)
                courseList = userDetails.course.all()

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

