# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20150209_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.CharField(default=b'Open', max_length=15, choices=[(b'Open', b'Open'), (b'Closed', b'Closed'), (b'Secret', b'Secret')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='group_members',
            field=models.ManyToManyField(to='users.UserProfile'),
            preserve_default=True,
        ),
    ]
