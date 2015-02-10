# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(default=b'first name', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='isTeacher',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(default=b'last name', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='school',
            field=models.CharField(default=b'school', max_length=500),
            preserve_default=True,
        ),
    ]
