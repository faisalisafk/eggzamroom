from django.shortcuts import render

from django.apps import apps

def index(request):
    user = request.user

    if user.is_authenticated:
        context = {'user_id':user.pk}
        #normal import not working so this way managed
        Teacher = apps.get_model('accounts', 'Teacher')
        temp = Teacher.objects.get(pk=user.pk)
        val = Teacher.objects.values()
        print(temp)
        for t in val:
            print(t)
        return render(request, 'teacher/teacher_courses.html', context)


