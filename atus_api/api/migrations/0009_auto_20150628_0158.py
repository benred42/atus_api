# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_householdmember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='householdmember',
            old_name='case_id',
            new_name='respondent',
        ),
    ]
