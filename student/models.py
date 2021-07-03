import uuid
from django.db import models

import accounts.models
from accounts.models import Student
from teacher.models import Course


class JoinCourse(models.Model):

    #course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default="Null")
    courses = models.ManyToManyField(Course, default='Null')

