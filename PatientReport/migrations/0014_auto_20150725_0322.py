# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0013_auto_20150725_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alignmentparameter',
            name='picture',
            field=models.ImageField(max_length=500, null=True, upload_to=b'', blank=True),
        ),
    ]
