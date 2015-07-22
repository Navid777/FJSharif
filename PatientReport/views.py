from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from PatientReport.forms import *
from PatientReport.models import Patient, Proficiency, AlignmentParameterName, Surgeon, Staff, Order


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
    return render(request, 'createSurgeon.html', {'surgeon_form':surgeon_form, 'user_form':user_form})


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
    return render(request, 'createStaff.html', {'staff_form':staff_form, 'user_form':user_form})


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
    return render(request, 'createPatient.html', {'patient_form': patient_form, 'user_form': user_form})


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
    return render(request, 'createPatient.html', {'patient_form': patient_form, 'user_form': user_form, 'edit': True})


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
    return render(request, 'createSurgeon.html', {'surgeon_form': surgeon_form, 'user_form': user_form, 'edit': True})


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
    return render(request, 'createStaff.html', {'staff_form': staff_form, 'user_form': user_form, 'edit': True})


@login_required
def home(request):
    user = request.user
    try:
        surgeon = user.surgeon
        return surgeon_home(request, surgeon.id)
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect(reverse('login'))

def test(request):
    return render(request, 'test3d.html')


@login_required
def surgeon_home(request, surgeon_id):
    surgeon = Surgeon.objects.get(id=surgeon_id)
    patients = Patient.objects.filter(order__surgeon=surgeon)
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
    return render(request, 'surgeonHome.html', {'surgeon': surgeon, 'patients': patients,
                                                'search_patient_form': search_patient_form,
                                                'search_results': search_results,
                                                'searched': searched})


@login_required
def view_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    surgeon = request.user.surgeon
    try:
        orders = Order.objects.filter(patient=patient, surgeon=surgeon)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    if orders.count() == 5:
        return HttpResponseRedirect(reverse('view_order', args=[orders[0].id]))
    else:
        return render(request, 'patient.html', {'patient': patient, 'orders': orders})


@login_required
def view_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('home'))
    surgeon = request.user.surgeon
    if order.surgeon != surgeon:
        return HttpResponseRedirect(reverse('home'))
    alignment_parameters = AlignmentParameterName.objects.filter(alignmentparameter__report__order=order).distinct()
    return render(request, 'order.html', {'surgeon': surgeon, 'order': order,
                                          'alignment_parameters': alignment_parameters})
