# Generated by Django 3.2.4 on 2021-06-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20210629_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='endTime',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='startTime',
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(default='8446d', max_length=30),
        ),
    ]
