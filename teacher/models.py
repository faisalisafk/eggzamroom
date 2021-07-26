import uuid
from django.db import models
from django.db.models.base import Model
from accounts.models import Teacher


class Course(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    subject = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    courseCode = models.CharField(
        max_length=7, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.courseCode:
            # Generate ID once, then check the db. If exists, keep trying.
            self.courseCode = uuid.uuid4().hex[:7].upper()
            while Course.objects.filter(courseCode=self.courseCode).exists():
                self.courseCode = uuid.uuid4().hex[:7].upper()
        super(Course, self).save(*args, **kwargs)


class Exam(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=50, null=False, blank=False)
    startTime = models.DateTimeField().auto_created
    endTime = models.DateTimeField().auto_created
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Form(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False,default="Untitled Form")
    description = models.TextField(max_length=100, null=False, blank=False,default="Untitled Description")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

class Question(models.Model):
    question_title = models.TextField(max_length=200, null=False, blank=False)
    question_type = models.CharField(max_length=20,null=False, blank=False)
    question_score = models.PositiveIntegerField(null=False,blank=False)
    form = models.ForeignKey(Form,on_delete=models.CASCADE, related_name='questions')

class Choice(models.Model):
    question_choice = models.CharField(max_length=20,null=False, blank=False)
    is_answer = models.BooleanField(null=False,blank=False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name='choices')