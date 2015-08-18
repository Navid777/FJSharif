# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0020_auto_20150818_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='name',
            field=models.CharField(default='salam', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preplanning',
            name='name',
            field=models.CharField(default='salam', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stlfile',
            name='pre_planning',
            field=models.ForeignKey(blank=True, to='PatientReport.PrePlanning', null=True),
        ),
    ]
