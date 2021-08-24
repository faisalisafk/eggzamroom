from student.models import Student
from django.contrib import admin
from .models import Student,Answer,SubmittedForm, StudentWindowDetectionLog
# Register your models here.

admin.site.register(Answer)
admin.site.register(SubmittedForm)
admin.site.register(StudentWindowDetectionLog)