# Generated by Django 3.0.6 on 2020-05-22 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0004_auto_20200522_0539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertask',
            old_name='user',
            new_name='author',
        ),
    ]
