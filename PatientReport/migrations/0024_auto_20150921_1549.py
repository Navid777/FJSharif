# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0023_auto_20150921_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stlfile',
            name='pre_planning',
            field=models.ForeignKey(blank=True, to='PatientReport.PrePlanning', null=True),
        ),
    ]
