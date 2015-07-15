# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='male',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='male',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='male',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surgeon',
            name='male',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
