# Generated by Django 3.2.4 on 2021-08-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_answer_givenanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='givenAnswer',
            field=models.IntegerField(),
        ),
    ]
