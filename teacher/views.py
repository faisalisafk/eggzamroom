from django.shortcuts import render


def index(request):
    user = request.user

    if user.is_authenticated:
        context = {'user_id': user.pk}
        return render(request, 'teacher/teacher_courses.html', context)


