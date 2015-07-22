# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0008_auto_20150715_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='x_ray',
            field=models.ImageField(null=True, upload_to=b'X-Ray/', blank=True),
        ),
    ]
