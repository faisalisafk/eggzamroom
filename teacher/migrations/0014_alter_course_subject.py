# Generated by Django 3.2.4 on 2021-07-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_alter_course_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(default='2ea41', max_length=30),
        ),
    ]