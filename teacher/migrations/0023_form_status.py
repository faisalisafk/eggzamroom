# Generated by Django 3.2.4 on 2021-08-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0022_auto_20210723_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
