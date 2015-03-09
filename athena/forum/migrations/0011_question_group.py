# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_remove_group_group_members'),
        ('forum', '0010_auto_20150302_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(blank=True, to='groups.Group', null=True),
            preserve_default=True,
        ),
    ]
