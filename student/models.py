import uuid
from django.db import models
from accounts.models import User
from teacher.models import Course


#import accounts.models
#from accounts.models import Student
#from teacher.models import Course


#class JoinCourse(models.Model):

    #course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #student = models.ForeignKey(Student, on_delete=models.CASCADE, default="Null")
    #courses = models.ManyToManyField(Course, pk=Student.user.username)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    studentID = models.IntegerField(unique=True, null=True)
    course = models.ManyToManyField(Course)
    # exams = models.ManyToManyField(Exam, through='TakenExam')
    # course = models.ManyToManyField(Course, related_name='interested_students')