# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0017_auto_20150802_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='mobile_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
