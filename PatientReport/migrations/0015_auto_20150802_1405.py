# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0014_auto_20150725_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='national_code',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
