# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0019_patient_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='STLFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=b'stl/')),
                ('guide', models.ForeignKey(blank=True, to='PatientReport.Guide', null=True)),
                ('pre_planning', models.ForeignKey(blank=True, to='PatientReport.PrePlanning', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='surgeon',
            name='national_code',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
