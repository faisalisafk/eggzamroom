from django.shortcuts import render

from django.apps import apps


def index(request):
    user = request.user

    if user.is_authenticated:
        context = {'user_id': user.pk}
        # normal import not working so this way managed
        User = apps.get_model('accounts', 'User')
        temp = User.objects.get(pk=user.pk)

        # logged in user detail in user
        context = {'user': temp}
        return render(request, 'teacher/teacher_courses.html', context)
