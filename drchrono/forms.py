from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DemographicForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'address', 'city',
                  'state', 'zip_code', 'cell_phone', 'email', 'emergency_contact_name', 'emergency_contact_phone',
                  'emergency_contact_relation', 'ethnicity', 'preferred_language', 'race', 'social_security_number']

    def __init__(self, *args, **kwargs):
        super(DemographicForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
