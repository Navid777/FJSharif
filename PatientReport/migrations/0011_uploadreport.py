# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0010_auto_20150725_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attributes', models.FileField(upload_to=b'temp')),
            ],
        ),
    ]
