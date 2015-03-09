# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20150302_2351'),
        ('users', '0003_auto_20150218_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='questions',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='downvotedAnswers',
            field=models.ManyToManyField(related_name='downvotedAnswers', to='forum.Answer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='upvotedAnswers',
            field=models.ManyToManyField(related_name='upvotedAnswers', to='forum.Answer'),
            preserve_default=True,
        ),
    ]
