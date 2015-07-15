# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0002_auto_20150712_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='male',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='male',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='staff',
            name='male',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='surgeon',
            name='male',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
