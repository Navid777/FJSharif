# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=400)),
                ('phone_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlignmentParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, choices=[(b'R', b'Right'), (b'L', b'Left')])),
                ('image', models.ImageField(upload_to=b'photos/%Y/%m/%d')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AlignmentParameterName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('abbreviation', models.CharField(unique=True, max_length=50)),
                ('max_value', models.FloatField(null=True, blank=True)),
                ('min_value', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('primary_diagnosis', models.CharField(max_length=3000, null=True, blank=True)),
                ('right_femur', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('left_femur', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('right_tibia', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('left_tibia', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('right_fibula', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('left_fibula', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('right_patella', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('left_patella', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('pelvis', models.FileField(null=True, upload_to=b'stl/', blank=True)),
                ('landmarks', models.FileField(null=True, upload_to=b'landmarks/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('national_code', models.CharField(unique=True, max_length=100)),
                ('picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('DOB', models.DateField()),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('description', models.TextField(max_length=3000, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preplanning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.ForeignKey(to='PatientReport.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Proficiency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('abbreviation', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('address', models.CharField(max_length=400)),
                ('phone_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=100)),
                ('national_code', models.CharField(unique=True, max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Surgeon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('national_code', models.CharField(unique=True, max_length=100)),
                ('picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('medical_id', models.CharField(max_length=100, unique=True, null=True, blank=True)),
                ('address', models.CharField(max_length=400, null=True, blank=True)),
                ('office_number', models.CharField(max_length=20, null=True, blank=True)),
                ('mobile_number', models.CharField(max_length=20, null=True, blank=True)),
                ('proficiency', models.ForeignKey(to='PatientReport.Proficiency')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='patient',
            field=models.ForeignKey(to='PatientReport.Patient'),
        ),
        migrations.AddField(
            model_name='order',
            name='report',
            field=models.ForeignKey(blank=True, to='PatientReport.Report', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(to='PatientReport.Staff'),
        ),
        migrations.AddField(
            model_name='order',
            name='surgeon',
            field=models.ForeignKey(to='PatientReport.Surgeon'),
        ),
        migrations.AddField(
            model_name='guide',
            name='order',
            field=models.ForeignKey(to='PatientReport.Order'),
        ),
        migrations.AddField(
            model_name='alignmentparameter',
            name='name',
            field=models.ForeignKey(to='PatientReport.AlignmentParameterName'),
        ),
        migrations.AddField(
            model_name='alignmentparameter',
            name='report',
            field=models.ForeignKey(to='PatientReport.Report'),
        ),
        migrations.AlterUniqueTogether(
            name='alignmentparameter',
            unique_together=set([('name', 'type', 'report')]),
        ),
    ]
