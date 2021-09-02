# Generated by Django 3.2.4 on 2021-08-30 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0023_form_status'),
        ('student', '0010_submittedform'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentWindowDetectionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(blank=True, max_length=5000, null=True)),
                ('end_time', models.CharField(blank=True, max_length=5000, null=True)),
                ('totalSeconds', models.IntegerField(blank=True, default=-1)),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.form')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]