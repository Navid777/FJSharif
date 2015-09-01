# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0021_auto_20150818_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stlfile',
            name='pre_planning',
            field=models.ForeignKey(blank=True, to='PatientReport.PrePlanning', null=True),
        ),
    ]
