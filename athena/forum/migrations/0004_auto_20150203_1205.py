# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20150128_2321'),
        ('forum', '0003_auto_20150128_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='answers',
            field=models.ManyToManyField(to='forum.Answer'),
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
            name='questions',
            field=models.ManyToManyField(to='forum.Question'),
            preserve_default=True,
        ),
    ]
