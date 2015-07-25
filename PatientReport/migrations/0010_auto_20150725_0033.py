# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0009_report_x_ray'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alignmentparameter',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'photos/%Y/%m/%d', blank=True),
        ),
    ]
