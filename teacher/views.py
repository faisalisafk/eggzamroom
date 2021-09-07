from student.views import submit
from django.http.response import JsonResponse
import requests, json
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
import pickle
from django.apps import apps
from accounts.models import User, Teacher
from .models import Course, Exam, Form, Question, Choice
from student.models import Student, StudentWindowDetectionLog, SubmittedForm
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


def saveFormTitle(request, examPk):
    if request.method == 'POST':
        titl = request.POST["title"]
        myform = Form.objects.filter(exam=Exam.objects.get(pk=examPk))
        myform.update(title=titl)
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def saveFormDes(request, examPk):
    if request.method == 'POST':
        des = request.POST["description"]
        myform = Form.objects.filter(exam=Exam.objects.get(pk=examPk))
        myform.update(description=des)
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def saveQuestion(request, examPk):
    if request.method == 'POST':
        myId = request.POST["quesId"]
        myQuesTitle = request.POST["myQuestion"]
        myQuestion = Question.objects.filter(pk=myId)
        myQuestion.update(question_title=myQuesTitle)
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def saveMark(request, examPk):
    if request.method == 'POST':
        myId = request.POST["quesId"]
        myMark = request.POST["mark"]
        myQuestion = Question.objects.filter(pk=myId)
        myQuestion.update(question_score=myMark)
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def editOption(request, examPk):
    if request.method == 'POST':
        myId = request.POST["optionId"]
        myOption = request.POST["myOption"]

        isChecked = json.loads(request.POST["isChecked"])
        choice = Choice.objects.filter(pk=myId)
        choice.update(question_choice=myOption, is_answer=isChecked)
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def deleteOption(request, examPk):
    if request.method == 'POST':
        # choice_id = request.POST.get('mcq_choice_id', False)
        choice_id = request.POST['mcq_choice_id']
        choice = Choice.objects.filter(pk=choice_id)
        choice.delete()
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def addOption(request, examPk):
    if request.method == 'POST':
        question_pk = request.POST['mcq_question_id']
        question = Question.objects.get(pk=question_pk)
        added_choice = Choice(question_choice="add new option", is_answer=False, question=question)
        added_choice.save()
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def addQuestion(request, examPk):
    if request.method == 'POST':
        exam = Exam.objects.get(pk=examPk)
        form = Form.objects.get(exam=exam)
        added_question = Question(question_title="New Question", question_type="mcq", question_score="1", form=form)
        added_question.save()
        tempPk = added_question.pk

        return JsonResponse({'status': 'Save', 'newques': tempPk})
    else:
        return JsonResponse({'status': 0})


def delQuestion(request, examPk):
    if request.method == 'POST':
        myQues = request.POST['del_qid']
        getQues = Question.objects.filter(pk=myQues)
        getQues.delete()
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})


def toggleForm(request, formPk):
    form = Form.objects.get(pk=formPk)
    exam = Exam.objects.get(pk=form.exam.pk)
    if form.status:
        form.status = False
        form.save()
        context = {'exam': exam,
                   'form': form}
        return render(request, 'teacher/form.html', context)

    else:
        form.status = True
        form.save()
        context = {'exam': exam,
                   'form': form}
        return render(request, 'teacher/form.html', context)


def viewScore(request, examPk):
    try:
        form = Form.objects.get(exam=Exam.objects.get(pk=examPk))
        log = StudentWindowDetectionLog.objects.filter(form=form)
        submitted = SubmittedForm.objects.filter(form=form)
        students = []
        for s in submitted:
            students.append(s.student.pk)
        print(students)
        context = {'form': form,
                   'submit': students,
                   'log': log}

        return render(request, 'teacher/viewScore.html', context)
    except:
        return render(request, 'teacher/404.html')
