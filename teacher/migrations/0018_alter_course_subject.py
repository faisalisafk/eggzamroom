# Generated by Django 3.2.4 on 2021-07-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0017_alter_course_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(default='91cc9', max_length=30),
        ),
    ]
