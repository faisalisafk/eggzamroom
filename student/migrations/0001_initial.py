# Generated by Django 3.2.4 on 2021-07-03 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0013_alter_course_subject'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(default='Null', to='teacher.Course')),
                ('student', models.ForeignKey(default='Null', on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
    ]