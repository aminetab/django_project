# Generated by Django 3.1.3 on 2021-09-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20210916_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='choice_submit',
            field=models.IntegerField(choices=[('', '---------')], null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='lesson',
            field=models.CharField(max_length=200),
        ),
    ]