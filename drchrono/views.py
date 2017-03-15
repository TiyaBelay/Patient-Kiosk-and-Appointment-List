#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib import messages

#Project
from .models import Doctor, Patient
from .forms import PatientForm, DemographicForm

#Python
import datetime
import requests, pytz

from drchrono.settings import SOCIAL_AUTH_DRCHRONO_KEY, SOCIAL_AUTH_DRCHRONO_SECRET


def index(request):
    """Sign In"""

    return render(request, 'index.html')


def authorize(request):
    """User authorizes application"""

    base_url = 'https://drchrono.com/o/authorize/'
    redirect_uri = 'http://localhost:8000/login'
    client_id = '2xMAgUko6q02uM8IDnWiNynNwqbhuc7dpgKMxHmE'
    scope = 'patients:read'
    url = base_url + "?redirect_uri={}&response_type=code&client_id={}&scope={}".format(redirect_uri, client_id, scope)

    return HttpResponseRedirect(url)


@login_required
def drchrono_login(request):
    """Drchrono Authorization and authentication"""

    if 'error' in request.GET:
        raise ValueError('Error authorizing application: %s' % request.GET['error'])

    response = requests.post('https://drchrono.com/o/token/', data={
        'code': request.GET['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://localhost:8000/login',
        'client_id': SOCIAL_AUTH_DRCHRONO_KEY,
        'client_secret': SOCIAL_AUTH_DRCHRONO_SECRET,
    })

    response.raise_for_status()
    data = response.json()
    print data

    # Saves these in database associated with the user
    access_token = data['access_token']
    refresh_token = data['refresh_token']
    expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])

    try:
        Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        user = Doctor(
            first_name='John', last_name='Smith', user=request.user, access_token=access_token, refresh_token=refresh_token,
            expires_timestamp=expires_timestamp
        )
        user.save()

    return HttpResponseRedirect(reverse('home'))


def home(request):
    """Doctor can pick to view appointment list or patient check in"""

    return render(request, 'home.html')


def check_in(request):
    """Patient Check-in"""

    form = PatientForm()
    return render(request, 'check_in.html', {'form': form})


def patient_demographic(request):
    """Patient chart that gets updated by patient on check in"""

    if request.method == "POST":
        form = PatientForm(request.POST)

        #if data is valid, query from what is in db, if not then add the new patient
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']

            patient = Patient.objects.filter(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)

            #trying to retrieve patient's data to display to the form and have the patient edit/update
            if patient.exists():
                demo_form = DemographicForm(request.POST, instance=patient[0])
                demo_form.save()
                return render(request, 'demographic.html')
            else:
                Patient.objects.create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
            return redirect('demographic')

        else:
            messages.error(request, "Error: Please enter your information.")

            return HttpResponseRedirect(reverse('check_in'))


    user = Doctor.objects.get(user=request.user)

    headers = {
        'Authorization': 'Bearer %s' % user.access_token,
    }

    patient_info = []
    patients_url = 'https://drchrono.com/api/patients'

    while patients_url:
        data = requests.get(patients_url, headers=headers).json()
        patient_info.append(data['results'])
        patients_url = data['next']

    for data_list in patient_info:
        for data in data_list:
            patient = Patient(patient_id=data['id'], first_name=data['first_name'], middle_name=data['middle_name'],
                              last_name=data['last_name'], date_of_birth=data['date_of_birth'], gender=data['gender'],
                              address=data['address'], city=data['city'], state=data['state'], zip_code=data['zip_code'],
                              cell_phone=data['cell_phone'], email=data['email'], ethnicity=data['ethnicity'],
                              preferred_language=data['preferred_language'], race=data['race'],
                              social_security_number=data['social_security_number'],
                              emergency_contact_name=data['emergency_contact_name'],
                              emergency_contact_phone=data['emergency_contact_phone'],
                              emergency_contact_relation=data['emergency_contact_relation'],
                              )
            patient.save()

    form = DemographicForm()

    return render(request, 'demographic.html', {'form': form,
                                                'patient_info': patient_info}
                  )


def edit_demographic(request):
    pass


def checked_in(request):
    """Patient completed check in."""

    # patient_obj = Patient.objects.get(patient_id=patient_id)
    #
    # if request.method == "POST":
    #     form = PatientForm(request.POST)
    #
    #     if form.is_valid():

    doc = Doctor.objects.get(user=request.user)

    return render(request, 'checked_in.html', {'doc': doc})


def set_appointment_status(request):
    """Set appointment status for patient to 'Arrived'"""

    pass


def make_appointments(request):
    """Patient creates appointments"""

    user = Doctor.objects.get(user=request.user)

    headers = {
        'Authorization': 'Bearer %s' % user.access_token,
    }

    data = {
        'doctor': user.doctor_id,
        'duration': 30,
        'office': 3456,
        'patient': 63536570,
        'scheduled_time': '2017-03-14T14:30:00',
    }
    url = 'https://drchrono.com/api/appointments'

    r = requests.post(url, data=data, headers=headers)


def appointments(request):
    """Lists all of today's appointments."""

    user = Doctor.objects.get(user=request.user)

    scope = 'calendar:read calendar:write clinical:read clinical:write'

    headers = {
        'Authorization': 'Bearer %s' % user.access_token,
    }

    appointment_info = []
    appointments_url = 'https://drchrono.com/api/appointments'

    while appointments_url:
        data = requests.get(appointments_url, scope, headers=headers).json()
        appointment_info.append(data['results'])
        appointments_url = data['next']

    return render(request, 'appointment.html', {'appointment_info': appointment_info})


def patient_wait_period(request):
    """Display how long a patient waited for"""
    pass


def average_wait_time(request):
    """Display average wait time for all patients"""
    pass


def drchrono_logout(request):
    """Log out"""

    logout(request)
    return HttpResponseRedirect('/')
