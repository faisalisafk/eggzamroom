import requests
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.apps import apps
from accounts.models import User
from teacher.models import Choice, Course, Exam, Form, Question
from student.models import Answer, Student
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
                    return redirect('/student/')
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


def examFormPage(request, examPk):
    exam = Exam.objects.get(pk=examPk)
    answered = Answer.objects.filter(student=request.user.pk,form=Form.objects.get(exam=Exam.objects.get(pk=examPk)))
    if not answered.exists():
        answered = []
    try:        
        form = Form.objects.get(exam=Exam.objects.get(pk=examPk))
        questions = form.questions.all()
        totalQuestion = questions.count()
        totalMark = 0
        for q in questions:
            totalMark = totalMark + q.question_score
    except Form.DoesNotExist:
        totalMark = 0
        form = []
        totalQuestion = 0
    context = {'exam': exam,
               'form': form,
               'totalQuestion': totalQuestion,
               'totalMark': totalMark,
               'answered' : answered,
               }
    return render(request, 'student/examForm.html', context)

def saveAnswer(request, examPk):
    temp = Answer.objects.filter(student=request.user.pk,question=request.POST["questionId"])
    if temp.exists():
        temp.update(givenAnswer=request.POST["optionChecked"]) 
    else:
        s = Student.objects.get(pk = request.user.pk)
        f = Form.objects.get(exam = Exam.objects.get(pk=examPk))
        q = Question.objects.get(pk = request.POST["questionId"])
        c = Choice.objects.get(pk = request.POST["optionChecked"])
        newAnswer = Answer(student=s,form=f,question=q,givenAnswer=c)
        newAnswer.save()
    return JsonResponse({'status': 'Save'})