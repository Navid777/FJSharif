# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0024_auto_20150921_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stlfile',
            name='pre_planning',
            field=models.ForeignKey(blank=True, to='PatientReport.PrePlanning', null=True),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='attributes',
            field=models.FileField(upload_to=b'temp', null=True, verbose_name=b'Report Attributes( an Excel file)', blank=True),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='guide_stls',
            field=models.FileField(upload_to=b'temp', null=True, verbose_name=b"Guides' STL Files( a Zip file)", blank=True),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='landmarks',
            field=models.FileField(upload_to=b'temp', null=True, verbose_name=b'Report Landmarks', blank=True),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='pre_stls',
            field=models.FileField(upload_to=b'temp', null=True, verbose_name=b"Preplannings' STL Files( a Zip file)", blank=True),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='report',
            field=models.FileField(upload_to=b'temp', null=True, verbose_name=b'Report( a PDF report file)', blank=True),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='zip_pictures',
            field=models.FileField(upload_to=b'temp', null=True, verbose_name=b'Report Pictures( a Zip file)', blank=True),
        ),
    ]
