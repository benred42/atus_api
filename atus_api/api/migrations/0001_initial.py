# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_1', models.CharField(max_length=2)),
                ('tier_2', models.CharField(max_length=4)),
                ('tier_3', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.FloatField()),
                ('activity', models.ForeignKey(to='api.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_wt', models.FloatField()),
                ('case_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent'),
        ),
    ]
