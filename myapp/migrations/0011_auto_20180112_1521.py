# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-12 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180112_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mode',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='mode',
            name='state',
        ),
        migrations.AddField(
            model_name='mode',
            name='milk',
            field=models.CharField(default='No', help_text='Do you want Milk', max_length=50),
        ),
        migrations.AddField(
            model_name='mode',
            name='sugar',
            field=models.CharField(default='Yes', help_text='Do you want sugar', max_length=50),
        ),
    ]
