import uuid
from django.db import models
from accounts.models import Teacher


class Course(models.Model):
    title = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    courseCode = models.CharField(max_length=7, null=True, blank=True, unique=True)
    def save(self, *args, **kwargs):
        if not self.courseCode:
            # Generate ID once, then check the db. If exists, keep trying.
            self.courseCode = uuid.uuid4().hex[:7].upper()
            while Course.objects.filter(courseCode=self.courseCode).exists():
                self.courseCode = uuid.uuid4().hex[:7].upper()
        super(Course, self).save(*args, **kwargs)





