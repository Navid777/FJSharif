# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0007_auto_20150714_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='alignmentparametername',
            name='direction',
            field=models.CharField(default='V', max_length=1, choices=[(b'H', b'Horizontal'), (b'V', b'Vertical')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alignmentparametername',
            name='type',
            field=models.CharField(max_length=2, choices=[(b'D', b'Degree'), (b'L', b'Length')]),
        ),
    ]
