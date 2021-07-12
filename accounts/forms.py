from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db import transaction

from accounts.models import User, Teacher
from student.models import Student


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    studentID = forms.IntegerField(label="StudentID", help_text='Student ID.',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}),
                                )
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}),
                                )

    class Meta:
        model = User
        fields = ("studentID", "email", "username", "firstName", "lastName", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'text-align': 'center'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.studentID = self.cleaned_data.get('studentID')
        student.save()
        # student.interests.add(*self.cleaned_data.get('interests')) // Add other attributes of students here later
        return user


class TeacherRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacherID = forms.IntegerField(label="teacherID", help_text='Teacher ID.',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}),
                                )
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ("teacherID", "email", "username", "firstName", "lastName", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'text-align': 'center'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.teacherID = self.cleaned_data.get('teacherID')
        teacher.save()
        # student.interests.add(*self.cleaned_data.get('interests')) // Add other attributes of students here later
        return user


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Email or password is invalid")
