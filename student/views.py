from django.core.exceptions import ObjectDoesNotExist

import student
import requests
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.apps import apps
from accounts.models import User
from teacher.models import Choice, Course, Exam, Form, Question
from student.models import Answer, Student ,SubmittedForm, StudentWindowDetectionLog
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
    try:    
        form=Form.objects.get(exam=Exam.objects.get(pk=examPk))
        sf = SubmittedForm.objects.filter(student=request.user.pk,form = form)
        exam = Exam.objects.get(pk=examPk)
        if sf.exists():
            context = {'form': form,
                    'exam': exam,}
            return render(request, 'student/already_submitted.html',context)
        if(form.status==False):
            return render(request,'student/notStarted.html')

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
                'answered': answered,
                }
        return render(request, 'student/examForm.html', context)
    except:
        return render(request,'teacher/404.html')

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

def submit(request, formPk):
    form = Form.objects.get(pk = formPk)
    newSubmittedForm = SubmittedForm(student=Student.objects.get(pk = request.user.pk),form = form)
    questions = form.questions.all()
    totalMarkObtain = 0

    answered = Answer.objects.filter(student=request.user.pk, form=form)

    for i in questions:
        for a in answered:
            if a.givenAnswer.is_answer and a.question == i:
                totalMarkObtain = totalMarkObtain + i.question_score

    newSubmittedForm.totalMarkObtain = totalMarkObtain
    newSubmittedForm.save()
    context = {'form': form,}
    return render(request, 'student/success.html',context)

def result(request, examPk):
    exam = Exam.objects.get(pk=examPk)
    form = Form.objects.get(exam=Exam.objects.get(pk=examPk))
    questions = form.questions.all()
    totalQuestion = questions.count()
    totalMark = 0
    totalMarkObtain = 0

    answered = Answer.objects.filter(student=request.user.pk, form=Form.objects.get(exam=Exam.objects.get(pk=examPk)))
    rightAnswer = []


    for i in questions:
        choices = Choice.objects.filter(question=i)
        for c in choices:
            if c.is_answer:
                rightAnswer.append(c)
        totalMark = totalMark + i.question_score
        for a in answered:
            if a.givenAnswer.is_answer and a.question == i:
                totalMarkObtain = totalMarkObtain + i.question_score
        #answer = Answer.objects.get(student=Student.objects.get(pk=request.user.pk), form=form, question=i)

        #choice = Choice.objects.get(question=i, )

        #Answer.objects.get(student=request.user.pk, question=Question.objects.get(id=i.id))
        #choice = Choice.objects.get(student=student, question=Question.objects.get(id=i.id))
        #choice = answer.givenAnswer
        #if choice.is_answer:
         #   totalMarkObtain = totalMarkObtain + i.question_score

    context = {'exam': exam,
               'form': form,
               'totalQuestion': totalQuestion,
               'totalMark': totalMark,
               'totalMarkObtain': totalMarkObtain,
               'answered': answered,
               'rightAnswer': rightAnswer,
               }
    return render(request, 'student/result.html', context)


def WindowDetectionLog(request, examPk):
    student = Student.objects.get(pk = request.user.pk)
    form = Form.objects.get(exam=Exam.objects.get(pk=examPk))
    log = StudentWindowDetectionLog.objects.filter(student=student,form=form)
    focused = request.POST.get("focused", 0)
    blurred = request.POST.get("blurred", 0)  


    if log.exists():   
        
        if blurred:       
            x = log[0].start_time + " <-> " + blurred
            log.update(start_time = x)
    
        elif focused:
            temp = log[0].start_time
            temp = temp.rsplit("<->",1)[1]
            temp = temp.split(",")[1]
            temp = temp.split(":")
            hour,minute,second = float(temp[0]),float(temp[1]),float(temp[2].split(" ")[0])
            
            foc = focused.split(",")[1]
            foc = foc.split(":")
            h,m,s = float(foc[0]),float(foc[1]),float(foc[2].split(" ")[0])

            total = int((h-hour) * 3600 + (m - minute) * 60 + (s - second))

            y =log[0].end_time + " <-> " + focused
            log.update(end_time = y)

            z = log[0].totalSeconds + total
            log.update(totalSeconds=z)
            

    else:
        if blurred:           
            log = StudentWindowDetectionLog(student=student, form=form, start_time= " <-> " +blurred, end_time="",totalSeconds=0)
            log.save()
            
        
        elif focused:
            log = StudentWindowDetectionLog(student=student, form=form, start_time="", end_time=focused)
            log.save()
            

    return JsonResponse({'status': 'Save'})

    # StudentWindowDetectionLog(student=student, form=form)
