# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20150306_0008'),
        ('forum', '0010_auto_20150302_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(default=None, to='groups.Group'),
            preserve_default=True,
        ),
    ]
