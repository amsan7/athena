# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20150209_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_members',
        ),
    ]
