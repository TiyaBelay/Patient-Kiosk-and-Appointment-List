from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth']


class DemographicForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'address', 'city',
                  'state', 'zip_code', 'cell_phone', 'email', 'emergency_contact_name', 'emergency_contact_phone',
                  'emergency_contact_relation', 'ethnicity', 'preferred_language', 'race', 'social_security_number']
