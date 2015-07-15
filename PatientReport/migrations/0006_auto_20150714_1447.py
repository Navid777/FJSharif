# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0005_proficiency_proficient_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='alignmentparametername',
            name='description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='alignmentparametername',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'alignmentParameters', blank=True),
        ),
        migrations.AddField(
            model_name='alignmentparametername',
            name='type',
            field=models.CharField(default='D', max_length=2, choices=[(b'D', b'degree'), (b'L', b'Length')]),
            preserve_default=False,
        ),
    ]
