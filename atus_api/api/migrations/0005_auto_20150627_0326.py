# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150626_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='tier_3',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='respondents',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='tier_1',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='tier_2',
        ),
        migrations.RemoveField(
            model_name='event',
            name='activity',
        ),
        migrations.AddField(
            model_name='event',
            name='activity',
            field=models.ManyToManyField(to='api.Activity'),
        ),
    ]
