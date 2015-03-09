# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_question_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
