from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import StudentRegistrationForm, AccountAuthenticationForm, TeacherRegistrationForm


# need to different login system !!!!
def login_view(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        if user.is_teacher:
            return redirect('/teacher/')
        else:
            return redirect('/student/')
    else:
        if request.POST:
            form = AccountAuthenticationForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email, password=password)
                if user:
                    login(request, user)
                    if user.is_teacher:
                        return redirect('/teacher/')
                    else:
                        return redirect('/student/')
                else:
                    return redirect("/login/")
        else:
            form = AccountAuthenticationForm()
        context['login_form'] = form
        return render(request, 'accounts/login.html', context)


def home_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/login/')
    else:
        if user.is_teacher:
            return redirect('/teacher/')
        elif user.is_student:
            return redirect('/student/')

def signup_view(request):
    context = {}
    if request.POST:
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/student/')
        else:
            context['registration_form'] = form

    else:
        form = StudentRegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/signup.html', context)


def teacher_signup_view(request):
    context = {}
    if request.POST:
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/teacher')
        else:
            context['registration_form'] = form

    else:
        form = TeacherRegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/signup_teacher.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login/')


def profile_view(request):
    # user = request.user
    # context = {}
    return render(request, 'accounts/profile.html')
