# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-01 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_courseorganization_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorganization',
            name='course',
        ),
    ]
