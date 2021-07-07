import uuid
from django.db import models
from accounts.models import User
from teacher.models import Course


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    studentID = models.IntegerField(unique=True, null=True)
    course = models.ManyToManyField(Course)
    # exams = models.ManyToManyField(Exam, through='TakenExam')
