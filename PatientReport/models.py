from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

GENDERS = (('M', 'Male'), ('F', 'Female'))


class Proficiency(models.Model):
    name = models.CharField(max_length=200, unique=True)
    abbreviation = models.CharField(max_length=50, unique=True)
    proficient_title = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name
    

class Surgeon(models.Model):
    national_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    medical_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    proficiency = models.ForeignKey(Proficiency)
    address = models.CharField(max_length=400, null=True, blank=True)
    office_number = models.CharField(max_length=20, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDERS)
    
    def __unicode__(self):
        return self.user.__unicode__()


class Staff(models.Model):
    picture = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    user = models.OneToOneField(User)
    position = models.CharField(max_length=100)
    national_code = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDERS)

    def __unicode__(self):
        return self.user.__unicode__()


class Admin(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    picture = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)

    def __unicode__(self):
        return self.user.__unicode__()

    
class Patient(models.Model):
    national_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    DOB = models.DateField()
    code = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(max_length=3000, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.user.__unicode__()

    def age(self):
        return datetime.now().date() - self.DOB

    
class Report(models.Model):
    name = models.CharField(max_length=300)
    x_ray = models.ImageField(null=True, blank=True, upload_to='X-Ray/')
    pdf = models.FileField(null=True, blank=True, upload_to='Report_PDFs/')
    
    def __unicode__(self):
        return self.name


class Order(models.Model):
    patient = models.ForeignKey(Patient)
    surgeon = models.ForeignKey(Surgeon)
    date = models.DateField(null=True, blank=True)
    primary_diagnosis = models.CharField(max_length=3000, null=True, blank=True)
    report = models.ForeignKey(Report, null=True, blank=True)
    staff = models.ForeignKey(Staff)
    right_femur = models.FileField(null=True, blank=True, upload_to='stl/')
    left_femur = models.FileField(null=True, blank=True, upload_to='stl/')
    right_tibia = models.FileField(null=True, blank=True, upload_to='stl/')
    left_tibia = models.FileField(null=True, blank=True, upload_to='stl/')
    right_fibula = models.FileField(null=True, blank=True, upload_to='stl/')
    left_fibula = models.FileField(null=True, blank=True, upload_to='stl/')
    right_patella = models.FileField(null=True, blank=True, upload_to='stl/')
    left_patella = models.FileField(null=True, blank=True, upload_to='stl/')
    pelvis = models.FileField(null=True, blank=True, upload_to='stl/')
    landmarks = models.FileField(null=True, blank=True, upload_to='landmarks/')
    description = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.patient.__unicode__() + '-' + self.surgeon.__unicode__() + '-' + str(self.id)

    
class Guide(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order)
    description = models.TextField()

    def __unicode__(self):
        return self.order.__unicode__()


class PrePlanning(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order)
    description = models.TextField()

    def __unicode__(self):
        return self.order.__unicode__()


class STLFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='stl/')
    guide = models.ForeignKey(Guide, null=True, blank=True)
    pre_planning = models.ForeignKey(PrePlanning, null=True, blank=True)

    def __unicode__(self):
        return self.name


class AlignmentParameterName(models.Model):
    name = models.CharField(max_length=200, unique=True)
    abbreviation = models.CharField(max_length=50, unique=True)
    max_value = models.FloatField(null=True, blank=True)
    min_value = models.FloatField(null=True, blank=True)
    picture = models.ImageField(upload_to='alignmentParameters', null=True, blank=True, max_length=500)
    description = models.CharField(max_length=1000, null=True, blank=True)
    TYPES = (('D', 'Degree'), ('L', 'Length'))
    DIRECTIONS = (('H', 'Horizontal'), ('V', 'Vertical'))
    direction = models.CharField(max_length=1, choices=DIRECTIONS)
    type = models.CharField(max_length=2, choices=TYPES)
    
    def __unicode__(self):
        return self.name


class AlignmentParameter(models.Model):
    name = models.ForeignKey(AlignmentParameterName)
    TYPES = (('R', 'Right'), ('L', 'Left'))
    type = models.CharField(max_length=1, choices=TYPES)
    picture = models.ImageField(null=True, blank=True, max_length=500)
    value = models.FloatField()
    report = models.ForeignKey(Report)

    class Meta:
        unique_together = ('name', 'type', 'report')
    
    def __unicode__(self):
        return self.name.__unicode__()


class UploadReport(models.Model):
    attributes = models.FileField(null=True, blank=True, upload_to='temp', verbose_name='Report Attributes( an Excel file)')
    zip_pictures = models.FileField(null=True, blank=True, upload_to='temp', verbose_name='Report Pictures( a Zip file)')
    report = models.FileField(null=True, blank=True, upload_to='temp', verbose_name='Report( a PDF report file)')
    landmarks = models.FileField(null=True, blank=True, upload_to='temp', verbose_name='Report Landmarks')
    guide_stls = models.FileField(null=True, blank=True, upload_to='temp', verbose_name='Guides\' STL Files( a Zip file)')
    pre_stls = models.FileField(null=True, blank=True, upload_to='temp', verbose_name='Preplannings\' STL Files( a Zip file)')

    def __unicode__(self):
        return 'upload_report_'+str(self.id)






    

    

