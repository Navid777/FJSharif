# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0011_uploadreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadreport',
            name='zip_pictures',
            field=models.FileField(default='s', upload_to=b'temp'),
            preserve_default=False,
        ),
    ]
