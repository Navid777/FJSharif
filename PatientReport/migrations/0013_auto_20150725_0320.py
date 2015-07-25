# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0012_uploadreport_zip_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alignmentparametername',
            name='picture',
            field=models.ImageField(max_length=500, null=True, upload_to=b'alignmentParameters', blank=True),
        ),
    ]
