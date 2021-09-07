from django.contrib import admin
from .models import User, Teacher
from student.models import Student


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
