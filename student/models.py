import uuid
from django.db import models
from django.db.models.base import Model
from accounts.models import User
from teacher.models import Course, Form, Question,Choice


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    studentID = models.IntegerField(unique=True, null=True)
    course = models.ManyToManyField(Course)
    # exams = models.ManyToManyField(Exam, through='TakenExam')

    def __str__(self):
        return self.user.username

class Answer(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    form = models.ForeignKey(Form,on_delete=models.CASCADE,blank=True,null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    givenAnswer = models.ForeignKey(Choice,on_delete=models.CASCADE)

class SubmittedForm(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    form = models.ForeignKey(Form,on_delete=models.CASCADE,blank=True,null=True)