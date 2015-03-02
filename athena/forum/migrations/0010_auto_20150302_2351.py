# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_question_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='body',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
    ]
