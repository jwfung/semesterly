# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2021-03-05 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0038_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='bed',
            field=models.CharField(default=-1, max_length=300),
        ),
        migrations.AlterField(
            model_name='home',
            name='chair',
            field=models.CharField(default=-1, max_length=300),
        ),
        migrations.AlterField(
            model_name='home',
            name='desk',
            field=models.CharField(default=-1, max_length=300),
        ),
    ]