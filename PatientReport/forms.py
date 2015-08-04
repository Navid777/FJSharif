from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from PatientReport.models import Surgeon, Proficiency, AlignmentParameterName, \
    Patient, Staff, UploadReport


class SurgeonForm(ModelForm):
    class Meta:
        model = Surgeon
        fields = ['national_code', 'medical_id', 'address', 'office_number', 'mobile_number', 'picture', 'proficiency', 'gender']

    def __init__(self, *args, **kwargs):
        super(SurgeonForm, self).__init__(*args, **kwargs)
        self.fields['national_code'].widget.attrs['placeholder'] = 'Enter your national code'
        self.fields['medical_id'].widget.attrs['placeholder'] = 'Enter your medical number'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter the address of your office'
        self.fields['office_number'].widget.attrs['placeholder'] = 'Office number'
        self.fields['mobile_number'].widget.attrs['placeholder'] = 'Mobile number'
        self.fields['picture'].widget.attrs['style'] = 'margin: 5px;'
        self.fields['proficiency'].widget.attrs['class'] = 'ui dropdown'
        self.fields['gender'].widget.attrs['class'] = 'ui dropdown'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['national_code', 'description', 'DOB', 'picture', 'gender', 'code', 'phone_number', 'mobile_number', 'address']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['national_code'].widget.attrs['placeholder'] = 'Enter your national code'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['DOB'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['code'].widget.attrs['placeholder'] = 'Enter the patient\'s code'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['mobile_number'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['picture'].widget.attrs['style'] = 'margin: 5px;'
        self.fields['gender'].widget.attrs['class'] = 'ui dropdown'

    def clean_national_code(self):
        return self.cleaned_data['national_code'] or None


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['address', 'phone_number', 'mobile_number', 'position', 'national_code', 'picture', 'gender']

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['national_code'].widget.attrs['placeholder'] = 'Enter your national code'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Office phone number'
        self.fields['mobile_number'].widget.attrs['placeholder'] = 'Mobile number'
        self.fields['picture'].widget.attrs['style'] = 'margin: 5px;'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter your address'
        self.fields['position'].widget.attrs['placeholder'] = 'Enter your position'
        self.fields['gender'].widget.attrs['class'] = 'ui dropdown'


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'


class UserEditForm(ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'


class ProficiencyForm(ModelForm):
    class Meta:
        model = Proficiency
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProficiencyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Proficiency name'
        self.fields['abbreviation'].widget.attrs['placeholder'] = 'Proficiency abbreviation'
        self.fields['proficient_title'].widget.attrs['placeholder'] = 'Proficient\'s title'


class AlignmentParameterNameForm(ModelForm):
    class Meta:
        model = AlignmentParameterName
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AlignmentParameterNameForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Alignment parameter name'
        self.fields['abbreviation'].widget.attrs['placeholder'] = 'Alignment parameter abbreviation'
        self.fields['min_value'].widget.attrs['placeholder'] = 'Enter the minimum value that this parameter can get'
        self.fields['max_value'].widget.attrs['placeholder'] = 'Enter the maximum value that this parameter can get'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter a description'


class SearchPatientForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name", required=False)
    last_name = forms.CharField(max_length=100, label="Last Name", required=False)
    national_code = forms.CharField(max_length=100, label="National Code", required=False)

    def __init__(self, *args, **kwargs):
        super(SearchPatientForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter the patient\'s first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter the patient\'s last name'
        self.fields['national_code'].widget.attrs['placeholder'] = 'Enter the patient\'s national code'


class SearchSurgeonForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name", required=False)
    last_name = forms.CharField(max_length=100, label="Last Name", required=False)
    proficiency = forms.ModelChoiceField(queryset=Proficiency.objects.all(), required=False)
    GENDERS = (('', '--------'), ('M', 'Male'), ('F', 'Female'))
    gender = forms.ChoiceField(choices=GENDERS, required=False)

    def __init__(self, *args, **kwargs):
        super(SearchSurgeonForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter the patient\'s first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter the patient\'s last name'


class UploadReportForm(forms.ModelForm):
    class Meta:
        model = UploadReport
        fields = '__all__'


