# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0004_auto_20150712_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='proficiency',
            name='proficient_title',
            field=models.CharField(default='Radiologist', unique=True, max_length=50),
            preserve_default=False,
        ),
    ]
