# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150627_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respondent',
            name='work_status',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
