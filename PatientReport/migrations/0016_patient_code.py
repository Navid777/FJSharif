# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0015_auto_20150802_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='code',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
