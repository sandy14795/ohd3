# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-02 16:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voteradm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='admission_answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='voteradm',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answers.admission_Answer'),
        ),
        migrations.AddField(
            model_name='voteradm',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
