# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2021-02-25 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0035_student_fav_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fav_number',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
    ]