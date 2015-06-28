# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150627_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdMember',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('hhmember_id', models.IntegerField()),
                ('age_edited', models.IntegerField()),
                ('relationship', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('age_flag', models.IntegerField()),
                ('relationship_flag', models.IntegerField()),
                ('gender_flag', models.IntegerField()),
                ('case_id', models.ForeignKey(to='api.Respondent')),
            ],
        ),
    ]
