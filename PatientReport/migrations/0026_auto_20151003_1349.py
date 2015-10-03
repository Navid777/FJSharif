# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0025_auto_20150921_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='proficiency',
            name='parent',
            field=models.ForeignKey(blank=True, to='PatientReport.Proficiency', null=True),
        ),
        migrations.AlterField(
            model_name='stlfile',
            name='pre_planning',
            field=models.ForeignKey(blank=True, to='PatientReport.PrePlanning', null=True),
        ),
        migrations.RemoveField(
            model_name='surgeon',
            name='proficiency',
        ),
        migrations.AddField(
            model_name='surgeon',
            name='proficiency',
            field=models.ManyToManyField(to='PatientReport.Proficiency'),
        ),
    ]
