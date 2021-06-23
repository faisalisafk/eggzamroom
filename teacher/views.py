from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'teacher/teacher_courses.html', context)
