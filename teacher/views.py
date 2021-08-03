from django.http.response import JsonResponse
import requests,json
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

from django.apps import apps
from accounts.models import User, Teacher
from .models import Course, Exam, Form,Question,Choice
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
                   'form': form,
                   'coursePk': coursePk}
        return render(request, 'teacher/exams.html', context)


def formPage(request, examPk):
    # First check if a form does not exists create a default form
    try:
        form = Form.objects.get(exam=Exam.objects.get(pk=examPk))
    except Form.DoesNotExist:
        print("got no form man!!!!")
        form = Form(exam=Exam.objects.get(pk=examPk))
        form.save()    
    
    exam = Exam.objects.get(pk=examPk)
    
    context = {'exam': exam,
                'form': form}
    return render(request, 'teacher/form.html', context)

def saveForm(request,examPk):
    if request.method=='POST':
        titl = request.POST["title"]
        des = request.POST["description"]
        myform = Form.objects.filter(exam=Exam.objects.get(pk=examPk))      
        myform.update(title=titl,description=des)
        return JsonResponse({'status':  'Save'})
    else:
        return JsonResponse({'status':  0})

def saveQuestion(request,examPk):
    if request.method=='POST':
        myId = request.POST["quesId"]
        myQuesTitle = request.POST["myQuestion"]
        myMark = request.POST["mark"]
        myQuestion = Question.objects.filter(pk=myId)
        myQuestion.update(question_title = myQuesTitle,question_score=myMark)
        return JsonResponse({'status':  'Save'})
    else:
        return JsonResponse({'status':  0})

def editOption(request,examPk):
    if request.method == 'POST':
        myId = request.POST["optionId"]
        myOption = request.POST["myOption"]
        
        isChecked = json.loads(request.POST["isChecked"])
        choice = Choice.objects.filter(pk=myId)
        choice.update(question_choice=myOption,is_answer = isChecked)
        return JsonResponse({'status':  'Save'})
    else:
        return JsonResponse({'status':  0})


def deletecourse(request, coursePk):
    if request.user.is_teacher:
        deletedcourse = Course.objects.get(pk=coursePk)
        deletedcourse.delete()

        form = CourseForm()
        userDetails = User.objects.get(pk=request.user.pk)
        courseList = Course.objects.filter(teacher=request.user.pk)
        context = {'user': userDetails,
                   'course': courseList,
                   'form': form}
        return render(request, 'teacher/teacher_courses.html', context)


def editCourse(request):
    if request.user.is_teacher:
        if request.method == 'POST':
            coursePk = request.POST.get('courseId')
            editdcourse = Course.objects.get(pk=coursePk)

            title = request.POST['title']
            subject = request.POST['subject']
            editdcourse.title = title
            editdcourse.subject = subject
            editdcourse.save()

        form = CourseForm()
        userDetails = User.objects.get(pk=request.user.pk)
        courseList = Course.objects.filter(teacher=request.user.pk)
        context = {'user': userDetails,
                   'course': courseList,
                   'form': form}
        return render(request, 'teacher/teacher_courses.html', context)
    else:
        return redirect('/login/')



def deleteexam(request, examPk):
    if request.user.is_teacher:
        deletedexam = Exam.objects.get(pk=examPk)
        coursePk = deletedexam.course.pk
        deletedexam.delete()

        form = ExamForm()
        exams = Exam.objects.filter(course=coursePk)
        context = {'exams': exams,
                   'form': form,
                   'coursePk': coursePk}
        return render(request, 'teacher/exams.html', context)
