# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_group_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='type',
            new_name='group_type',
        ),
    ]
