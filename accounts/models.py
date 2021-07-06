from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from teacher.models import Course

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email address is required for users.")
        if not username:
            raise ValueError("Username is required for users.")

        user = self.model(email=self.normalize_email(email),
                          username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email),
                                username=username, password=password)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # used for login -_-
    REQUIRED_FIELDS = ['username', ]

    objects = UserAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True





class Exam(models.Model):
    pass






class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacherID = models.IntegerField(unique=True, null=True)
