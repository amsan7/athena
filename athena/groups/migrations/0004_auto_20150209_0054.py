# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_auto_20150209_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupuserjoin',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupuserjoin',
            name='user',
        ),
        migrations.DeleteModel(
            name='GroupUserJoin',
        ),
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.AddField(
            model_name='group',
            name='creator_username',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='group_members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
