# Generated by Django 3.2.4 on 2021-08-30 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_studentwindowdetectionlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentwindowdetectionlog',
            name='totalSeconds',
        ),
    ]
