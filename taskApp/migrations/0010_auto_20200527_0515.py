# Generated by Django 3.0.6 on 2020-05-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0009_auto_20200523_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='label',
            field=models.CharField(max_length=264),
        ),
    ]