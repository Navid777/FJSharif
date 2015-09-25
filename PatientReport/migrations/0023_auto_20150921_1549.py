# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PatientReport', '0022_auto_20150901_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preplanning',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='pdf',
            field=models.FileField(null=True, upload_to=b'Report_PDFs/', blank=True),
        ),
        migrations.AddField(
            model_name='uploadreport',
            name='guide_stls',
            field=models.FileField(default=0, upload_to=b'temp', verbose_name=b"Guides' STL Files( a Zip file)"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadreport',
            name='landmarks',
            field=models.FileField(default=0, upload_to=b'temp', verbose_name=b'Report Landmarks'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadreport',
            name='pre_stls',
            field=models.FileField(default=0, upload_to=b'temp', verbose_name=b"Preplannings' STL Files( a Zip file)"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadreport',
            name='report',
            field=models.FileField(default=0, upload_to=b'temp', verbose_name=b'Report( a PDF report file)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stlfile',
            name='pre_planning',
            field=models.ForeignKey(blank=True, to='PatientReport.PrePlanning', null=True),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='attributes',
            field=models.FileField(upload_to=b'temp', verbose_name=b'Report Attributes( an Excel file)'),
        ),
        migrations.AlterField(
            model_name='uploadreport',
            name='zip_pictures',
            field=models.FileField(upload_to=b'temp', verbose_name=b'Report Pictures( a Zip file)'),
        ),
    ]
