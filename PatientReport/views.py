import os
from zipfile import ZipFile
import django
from django.contrib.auth import authenticate, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from openpyxl import load_workbook
from os import listdir
from FJSharif.settings import MEDIA_URL, MEDIA_ROOT
from PatientReport import models

from PatientReport.forms import *
from PatientReport.models import Patient, Proficiency, AlignmentParameterName, Surgeon, Staff, Order, AlignmentParameter, \
    Report, PrePlanning, Guide, STLFile


# Create your views here.

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def create_surgeon(request):
    user_form = UserForm()
    surgeon_form = SurgeonForm()
    if request.method == 'POST':
        surgeon_form = SurgeonForm(request.POST, request.FILES)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and surgeon_form.is_valid():
            user = user_form.save()
            surgeon = surgeon_form.save(commit=False)
            surgeon.user = user
            surgeon.save()
            return HttpResponseRedirect(reverse('manage_surgeons'))
    return render(request, 'createSurgeon.html', {'surgeon_form': surgeon_form, 'user_form': user_form})


def create_staff(request):
    user_form = UserForm()
    staff_form = StaffForm()
    if request.method == 'POST':
        staff_form = StaffForm(request.POST, request.FILES)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and staff_form.is_valid():
            user = user_form.save()
            surgeon = staff_form.save(commit=False)
            surgeon.user = user
            surgeon.save()
    return render(request, 'createStaff.html', {'staff_form': staff_form, 'user_form': user_form})


@login_required
def create_patient(request):
    user_form = UserForm()
    patient_form = PatientForm()
    if request.method == 'POST':
        patient_form = PatientForm(request.POST, request.FILES)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            return HttpResponseRedirect(reverse('manage_patients'))
    return render(request, 'createPatient.html', {'patient_form': patient_form, 'user_form': user_form})


@login_required
def create_report(request):
    upload_report_form = UploadReportForm()
    if request.method == 'POST':
        upload_report_form = UploadReportForm(request.POST, request.FILES)
        if upload_report_form.is_valid():
            upload_report = upload_report_form.save()
            create_report_with_files(1, upload_report.attributes.path, upload_report.zip_pictures.path)
    return render(request, 'createReport.html', {'upload_report_form': upload_report_form})


@login_required
def create_order(request, patient_id=None, surgeon_id=None, has_properties=False):
    patient = None
    if patient_id:
        patient = Patient.objects.get(id=patient_id)
    surgeon = None
    if surgeon_id:
        surgeon = Surgeon.objects.get(id=surgeon_id)
    if has_properties == 'True' or has_properties == 'true':
        has_properties = True
    search_patient_form = SearchPatientForm()
    search_surgeon_form = SearchSurgeonForm()
    patient_search_results = Patient.objects.all()
    surgeon_search_results = Surgeon.objects.all()
    upload_report_form = UploadReportForm()
    if request.method == 'POST':
        if 'search_patient' in request.POST:
            search_patient_form = SearchPatientForm(request.POST)
            patient_search_results = Patient.objects.filter(
                user__first_name__contains=search_patient_form.cleaned_data['first_name'],
                user__last_name__contains=search_patient_form.cleaned_data['last_name'],
                national_code__contains=search_patient_form.cleaned_data['national_code'])
        if 'search_surgeon' in request.POST:
            search_surgeon_form = SearchSurgeonForm(request.POST)
            if search_surgeon_form.is_valid():
                surgeon_search_results = Surgeon.objects.filter(
                    user__first_name__contains=search_surgeon_form.cleaned_data['first_name'],
                    user__last_name__contains=search_surgeon_form.cleaned_data['last_name'],
                    )
                if search_surgeon_form.cleaned_data['gender'] != '':
                    surgeon_search_results = surgeon_search_results.filter(gender=search_surgeon_form.cleaned_data['gender'])
                if search_surgeon_form.cleaned_data['proficiency'] is not None:
                    surgeon_search_results = surgeon_search_results.filter(proficiency=search_surgeon_form.cleaned_data['proficiency'])
        if 'upload_report' in request.POST:
            upload_report_form = UploadReportForm(request.POST, request.FILES)
            if upload_report_form.is_valid():
                upload_report = upload_report_form.save()
                order = Order(staff=request.user.staff, patient=patient, surgeon=surgeon)
                order.save()
                if upload_report.guide_stls:
                    create_guide_with_files(order.id, upload_report.guide_stls.path)
                if upload_report.zip_pictures and upload_report.attributes:
                    report = Report(name="report")
                    report.save()
                    order.report = report
                    order.save()
                    if upload_report.landmarks:
                        order.landmarks = upload_report.landmarks
                    if upload_report.report:
                        report.pdf = upload_report.report
                    create_report_with_files(order.id, upload_report.attributes.path, upload_report.zip_pictures.path)
                else:
                    if upload_report.landmarks:
                        order.landmarks = upload_report.landmarks
                        order.save()
                    if upload_report.report:
                        report = Report(name='report')
                        report.pdf = upload_report.report
                        report.save()
                        order.report = report
                        order.save()
                if upload_report.pre_stls:
                    create_pre_planning_with_files(order.id, upload_report.pre_stls.path)
                return HttpResponseRedirect(reverse('manage_orders'))


    return render(request, 'createOrder.html', {'search_patient_form': search_patient_form,
                                                'search_surgeon_form': search_surgeon_form,
                                                'upload_report_form': upload_report_form,
                                                'patient_search_results': patient_search_results,
                                                'surgeon_search_results': surgeon_search_results,
                                                'patient': patient,
                                                'surgeon': surgeon,
                                                'has_properties': has_properties, })


#TODO: Complete this view
def manage_orders(request):
    orders = Order.objects.all()
    return render(request, 'manageOrders.html', {'orders': orders})


def create_proficiency(request):
    form = ProficiencyForm()
    if request.method == 'POST':
        form = ProficiencyForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'createProficiency.html', {'form': form})


def create_alignment_parameter_name(request):
    form = AlignmentParameterNameForm()
    if request.method == 'POST':
        form = AlignmentParameterNameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage_alignment_parameter_names'))
    return render(request, 'createAlignmentParameterName.html', {'form': form})


def edit_proficiency(request, proficiency_id):
    proficiency = Proficiency.objects.get(id=proficiency_id)
    form = ProficiencyForm(instance=proficiency)
    if request.method == 'POST':
        form = ProficiencyForm(request.POST, instance=proficiency)
        if form.is_valid():
            form.save()
    return render(request, 'createProficiency.html', {'form': form, 'edit': True})


def edit_alignment_parameter_name(request, alignment_parameter_name_id):
    alignment_parameter_name = AlignmentParameterName.objects.get(id = alignment_parameter_name_id)
    form = AlignmentParameterNameForm(instance=alignment_parameter_name)
    if request.method == 'POST':
        form = AlignmentParameterNameForm(request.POST, instance=alignment_parameter_name)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage_alignment_parameter_names'))
    return render(request, 'createAlignmentParameterName.html', {'form': form, 'edit': True})


def edit_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    user = patient.user
    user_form = UserEditForm(instance=user)
    patient_form = PatientForm(instance=patient)
    if request.method == 'POST':
        patient_form = PatientForm(request.POST, request.FILES, instance=patient)
        user_form = UserEditForm(request.POST, instance=user)
        if user_form.is_valid() and patient_form.is_valid():
            user_form.save()
            patient_form.save()
            return HttpResponseRedirect(reverse('manage_patients'))
    return render(request, 'createPatient.html', {'patient_form': patient_form, 'user_form': user_form, 'edit': True, 'patient': patient})


def edit_surgeon(request, surgeon_id):
    surgeon = Surgeon.objects.get(id=surgeon_id)
    user = surgeon.user
    user_form = UserEditForm(instance=user)
    surgeon_form = SurgeonForm(instance=surgeon)
    if request.method == 'POST':
        surgeon_form = SurgeonForm(request.POST, request.FILES, instance=surgeon)
        user_form = UserEditForm(request.POST, instance=user)
        if user_form.is_valid() and surgeon_form.is_valid():
            user_form.save()
            surgeon_form.save()
            return HttpResponseRedirect(reverse('manage_surgeons'))
    return render(request, 'createSurgeon.html', {'surgeon_form': surgeon_form, 'user_form': user_form, 'edit': True,
                                                  'surgeon': surgeon})


def edit_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    user = staff.user
    user_form = UserEditForm(instance=user)
    staff_form = StaffForm(instance=staff)
    if request.method == 'POST':
        staff_form = StaffForm(request.POST, request.FILES, instance=staff)
        user_form = UserEditForm(request.POST, instance=user)
        if user_form.is_valid() and staff_form.is_valid():
            user_form.save()
            staff_form.save()
    return render(request, 'createStaff.html', {'staff_form': staff_form, 'user_form': user_form, 'edit': True, 'staff': staff})


def edit_order(request, order_id):
    return HttpResponseRedirect(reverse('manage_orders'))


@login_required
def home(request):
    user = request.user
    try:
        surgeon = user.surgeon
        return surgeon_home(request, surgeon.id)
    except ObjectDoesNotExist:
        pass
    try:
        patient = user.patient
        return patient_home(request)
    except ObjectDoesNotExist:
        pass
    try:
        staff = user.staff
        return staff_home(request)
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect(reverse('login'))




@login_required
def surgeon_home(request, surgeon_id):
    surgeon = Surgeon.objects.get(id=surgeon_id)
    patients = Patient.objects.filter(order__surgeon=surgeon).distinct()
    search_patient_form = SearchPatientForm()
    search_results = None
    searched = False
    if request.method == 'POST':
        if 'search_patient' in request.POST:
            search_patient_form = SearchPatientForm(request.POST)
            if search_patient_form.is_valid():
                search_results = patients.filter(
                    user__first_name__contains=search_patient_form.cleaned_data['first_name'],
                    user__last_name__contains=search_patient_form.cleaned_data['last_name'],
                    national_code__contains=search_patient_form.cleaned_data['national_code'])
                searched = True
    return render(request, 'surgeonHome.html', {'patients': patients,
                                                'search_patient_form': search_patient_form,
                                                'search_results': search_results,
                                                'searched': searched})


@login_required
def patient_home(request):
    patient = request.user.patient
    orders = Order.objects.filter(patient=patient)
    return render(request, 'patient.html', {'patient': patient, 'orders': orders})


@login_required
def staff_home(request):
    return render(request, 'staffHome.html')


@login_required
def view_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    try:
        surgeon = request.user.surgeon
        orders = Order.objects.filter(patient=patient, surgeon=surgeon)
    except ObjectDoesNotExist:
        orders = Order.objects.filter(patient=patient)
    return render(request, 'patient.html', {'patient': patient, 'orders': orders})


@login_required
def view_report(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    alignment_parameters = AlignmentParameterName.objects.filter(alignmentparameter__report__order=order).distinct()
    return render(request, 'report.html', {'order': order,
                                           'alignment_parameters': alignment_parameters,})


@login_required
def view_guides(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    guides = Guide.objects.filter(order=order)
    return render(request, 'guides.html', {'order': order,
                                           'guides': guides})


@login_required
def view_pre_plannings(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    pre_plannings = PrePlanning.objects.filter(order=order)
    return render(request, 'prePlannings.html', {'order': order,
                                           'pre_plannings': pre_plannings})


@login_required
def view_patients(request, surgeon_id):
    surgeon = Surgeon.objects.get(id=surgeon_id)
    patients = Patient.objects.filter(order__surgeon=surgeon).distinct()
    return render(request, 'patients.html', {'surgeon': surgeon, 'patients': patients})


@login_required
def manage_patients(request, page_num=1):
    page_num = int(page_num)
    patient_per_page = 12
    patients = Patient.objects.all()
    search_patient_form = SearchPatientForm()
    search_results = Patient.objects.all()
    if (page_num-1)*patient_per_page >= search_results.count():
        return HttpResponseRedirect(reverse('manage_patients'))
    lower_bound = (page_num-1)*patient_per_page
    upper_bound = max(page_num*patient_per_page-1, search_results.count()-1)
    if request.method == 'POST':
        if 'search_patient' in request.POST:
            search_patient_form = SearchPatientForm(request.POST)
            if search_patient_form.is_valid():
                search_results = patients.filter(
                    user__first_name__contains=search_patient_form.cleaned_data['first_name'],
                    user__last_name__contains=search_patient_form.cleaned_data['last_name'],
                    national_code__contains=search_patient_form.cleaned_data['national_code'])
                if (page_num-1)*patient_per_page >= search_results.count():
                    page_num = 1
                lower_bound = (page_num-1)*patient_per_page
                upper_bound = max(page_num*patient_per_page-1, search_results.count()-1)
    return render(request, 'managePatients.html', {'patients': patients,
                                                   'search_patient_form': search_patient_form,
                                                   'search_results': search_results[lower_bound:upper_bound]})


@login_required
def manage_surgeons(request, page_num=1):
    page_num = int(page_num)
    surgeon_per_page = 12
    surgeons = Surgeon.objects.all()
    search_surgeon_form = SearchSurgeonForm()
    search_results = Surgeon.objects.all()
    if (page_num-1)*surgeon_per_page >= search_results.count():
        return HttpResponseRedirect(reverse('manage_surgeons'))
    lower_bound = (page_num-1)*surgeon_per_page
    upper_bound = max(page_num*surgeon_per_page-1, search_results.count()-1)
    if request.method == 'POST':
        if 'search_surgeon' in request.POST:
            search_surgeon_form = SearchSurgeonForm(request.POST)
            if search_surgeon_form.is_valid():
                search_results = surgeons.filter(
                    user__first_name__contains=search_surgeon_form.cleaned_data['first_name'],
                    user__last_name__contains=search_surgeon_form.cleaned_data['last_name'],
                    )
                if search_surgeon_form.cleaned_data['gender'] != '':
                    search_results = search_results.filter(gender=search_surgeon_form.cleaned_data['gender'])
                if search_surgeon_form.cleaned_data['proficiency'] is not None:
                    search_results = search_results.filter(proficiency=search_surgeon_form.cleaned_data['proficiency'])
                if (page_num-1)*surgeon_per_page >= search_results.count():
                    page_num = 1
                lower_bound = (page_num-1)*surgeon_per_page
                upper_bound = max(page_num*surgeon_per_page-1, search_results.count()-1)
    return render(request, 'manageSurgeons.html', {'surgeons': surgeons,
                                                   'search_surgeon_form': search_surgeon_form,
                                                   'search_results': search_results[lower_bound:upper_bound]})


@login_required
def manage_proficiencies(request):
    proficiencies = Proficiency.objects.all()
    return render(request, 'manageProficiencies.html', {'proficiencies': proficiencies})


@login_required
def manage_alignment_parameter_names(request):
    parameters = AlignmentParameterName.objects.all()
    return render(request, 'manageAlignmentParameterNames.html', {'parameters': parameters})


def create_report_with_files(order_id, xlsx_path, zip_path):
    order = Order.objects.get(id=order_id)
    report = order.report
    patient = order.patient
    zip_file = ZipFile(zip_path)
    pictures_root = MEDIA_ROOT+'/alignment_pictures/report'+str(report.id)
    pictures_url = MEDIA_URL+'alignment_pictures/report'+str(report.id)
    zip_file.extractall(pictures_root)
    xlsx_file = load_workbook(xlsx_path)
    sheet = xlsx_file['Alignment']
    for row in sheet.rows:
        try:
            parameter_name = AlignmentParameterName.objects.get(name=row[0].value)
            AlignmentParameter(name=parameter_name, report=report, value=row[2].value, type='R',
                               picture=pictures_url+'/'+parameter_name.name+'_R.jpg').save()
            AlignmentParameter(name=parameter_name, report=report, value=row[3].value, type='L',
                               picture=pictures_url+'/'+parameter_name.name+'_L.jpg').save()
        except ObjectDoesNotExist:
            pass


def create_guide_with_files(order_id, zip_path):
    zip_file = ZipFile(zip_path)
    order = Order.objects.get(id=order_id)
    pictures_root = MEDIA_ROOT+'/guide_stl_files/order'+str(order_id)+'/guide'+str(order.guide_set.all().count())
    pictures_url = MEDIA_URL+'guide_stl_files/order'+str(order_id)+'/guide'+str(order.guide_set.all().count())
    zip_file.extractall(pictures_root)
    guide = Guide(order=order, name='temp_name', description='temp_description')
    guide.save()
    for f in listdir(pictures_root.replace('\\', '/')):
        stl_file = STLFile(name=f, guide=guide, file=pictures_url+'/'+f)
        stl_file.save()


def create_pre_planning_with_files(order_id, zip_path):
    zip_file = ZipFile(zip_path)
    order = Order.objects.get(id=order_id)
    pictures_root = MEDIA_ROOT+'/preplanning_stl_files/order'+str(order_id)+'/preplanning'+str(order.preplanning_set.all().count())
    pictures_url = MEDIA_URL+'guide_stl_files/order'+str(order_id)+'/preplanning'+str(order.preplanning_set.all().count())
    zip_file.extractall(pictures_root)
    preplanning = PrePlanning(order=order, name='temp_name', description='temp_description')
    preplanning.save()
    for f in listdir(pictures_root.replace('\\', '/')):
        stl_file = STLFile(name=f, pre_planning=preplanning, file=pictures_url+'/'+f)
        stl_file.save()


def test(request):
    upload_report = UploadReport.objects.get(id=23)
    path = upload_report.guide_stls.path
    pictures_root = MEDIA_ROOT+'/guide_stl_files/order'+str(14)+'/guide'+str(0)
    pictures_url = MEDIA_URL+'/guide_stl_files/order'+str(14)+'/guide'+str(0)
    x = 0
    for f in listdir(pictures_root.replace('\\', '/')):
        print f
        x = f
    return HttpResponseRedirect(pictures_url+'/'+x)


@login_required
def ajax_delete_patient(request, patient_id):
    Patient.objects.get(id=patient_id).delete()
    return render(request, 'json/success.json')


@login_required
def ajax_delete_surgeon(request, surgeon_id):
    Surgeon.objects.get(id=surgeon_id).delete()
    return render(request, 'json/success.json')


@login_required
def ajax_delete_alignment_parameter_name(request, parameter_id):
    AlignmentParameterName.objects.get(id=parameter_id).delete()
    return render(request, 'json/success.json')


@login_required
def ajax_delete_order(request, order_id):
    Order.objects.get(id=order_id).delete()
    return render(request, 'json/success.json')

