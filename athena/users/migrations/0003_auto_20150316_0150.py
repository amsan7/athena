# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
        ('groups', '0004_remove_group_group_members'),
        ('users', '0002_auto_20150309_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='downvotedAnswers',
            field=models.ManyToManyField(related_name='downvotedAnswers', to='forum.Answer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(to='groups.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='upvotedAnswers',
            field=models.ManyToManyField(related_name='upvotedAnswers', to='forum.Answer'),
            preserve_default=True,
        ),
    ]
