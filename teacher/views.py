from django.shortcuts import render

from django.apps import apps
from accounts.models import User
from .models import Course

def index(request):
    user = request.user

    if user.is_authenticated:
        context = {'user_id': user.pk}
        # normal import not working so this way managed

        userDetails = User.objects.get(pk=user.pk)
        courseList = Course.objects.filter(teacher=user.pk)
        # logged in user detail in user

        print(courseList)
        context = {'user': userDetails,
                   'course': courseList,}
        return render(request, 'teacher/teacher_courses.html', context)
