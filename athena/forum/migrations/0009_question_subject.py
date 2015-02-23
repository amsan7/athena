# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20150209_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(default=b'Math', max_length=15, choices=[(b'Math', b'Math'), (b'Physics', b'Physics'), (b'Chemistry', b'Chemistry'), (b'Biology', b'Biology')]),
            preserve_default=True,
        ),
    ]
