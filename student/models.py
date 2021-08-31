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
        return self.user.firstName + " " + self.user.lastName

class Answer(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    form = models.ForeignKey(Form,on_delete=models.CASCADE,blank=True,null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    givenAnswer = models.ForeignKey(Choice,on_delete=models.CASCADE)

class SubmittedForm(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    form = models.ForeignKey(Form,on_delete=models.CASCADE,blank=True,null=True)


class StudentWindowDetectionLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.CharField(max_length=5000, blank=True, null=True)
    end_time = models.CharField(max_length=5000, blank=True, null=True)
    totalSeconds = models.IntegerField(null=True)

    def __str__(self):
        return self.student.user.username + "'s browser focus checks for the exam of" + self.form.exam.title
