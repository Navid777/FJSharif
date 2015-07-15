# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0006_auto_20150714_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alignmentparameter',
            old_name='image',
            new_name='picture',
        ),
    ]
