# Generated by Django 3.1.3 on 2021-09-18 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0020_auto_20210918_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='lesson',
        ),
    ]
