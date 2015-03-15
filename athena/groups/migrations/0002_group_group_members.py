# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150309_2035'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_members',
            field=models.ManyToManyField(to='users.UserProfile'),
            preserve_default=True,
        ),
    ]
