# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_activity_respondents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respondent',
            name='id',
        ),
        migrations.AlterField(
            model_name='respondent',
            name='case_id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
