# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0003_auto_20150712_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='male',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='male',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='male',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='surgeon',
            old_name='male',
            new_name='gender',
        ),
    ]
