from django.contrib import admin
from .models import Course,Exam,Form,Question,Choice

admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Choice)