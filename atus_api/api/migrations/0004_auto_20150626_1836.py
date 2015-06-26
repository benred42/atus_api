# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150626_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondent',
            name='age_edited',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='childcare_minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='education_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='eldercare_minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='employment_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='gender',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='has_multiple_jobs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='household_children',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='is_hispanic',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='is_holiday',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='is_student',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='metropolitan_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='partner_employed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='partner_present',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='partner_work_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='race',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='school_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='weekly_earnings_main',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='weekly_hours_worked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='work_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respondent',
            name='youngest_child_age',
            field=models.IntegerField(default=0),
        ),
    ]
