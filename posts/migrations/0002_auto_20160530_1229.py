# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-30 06:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 30, 12, 29, 38, 668000)),
        ),
        migrations.AddField(
            model_name='placement',
            name='ip',
            field=models.CharField(default='none', max_length=40),
        ),
        migrations.AddField(
            model_name='placement',
            name='session',
            field=models.CharField(default='none', max_length=40),
        ),
    ]
