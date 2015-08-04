# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0016_patient_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='code',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
