# Generated by Django 3.1.3 on 2021-09-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_auto_20210916_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='lesson',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
