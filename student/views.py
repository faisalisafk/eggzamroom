from django.shortcuts import render,redirect
from accounts.models import User
from django.contrib.auth import logout

# Create your views here.
def dashboard_student(request):

    if request.user.is_authenticated:
        if request.user.is_student:
            studentDetails = User.objects.get(pk=request.user.pk)
            context = {'student': studentDetails}
            print('ok')
            return render(request, 'student/dashboard_student.html', context)
        else:
            print('views 13')
            logout(request)
            return redirect('/login/')
    else:
        print('views 17')
        return redirect('/login/')