# Generated by Django 3.1.3 on 2021-09-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0022_auto_20210918_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_submitted',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_submitted',
            field=models.ManyToManyField(to='onlinecourse.Submission'),
        ),
    ]