from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'patient_code': 'Patient Code',
            'email': 'Email',
            'mobile': 'Mobile Number',
            'gender': 'Gender',
            'next_of_kin_name': 'Next of Kin Name',
            'next_of_kin_contact': 'Next of Kin Contact',
            'medical_allergies': 'Medical Allergies',
            'blood_group': 'Blood Group',
            'surgery': 'Undergone Surgery Before'
        }
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['blood_group'].empty_label = "Select"
        self.fields['surgery'].empty_label = "Select"