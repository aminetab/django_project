# Generated by Django 3.1.3 on 2021-09-18 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0018_submission_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.choice'),
        ),
    ]
