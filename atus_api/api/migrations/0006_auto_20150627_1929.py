# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150627_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respondent',
            name='age_edited',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
