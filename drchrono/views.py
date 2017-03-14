#Django
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from models import Doctor
from .forms import PatientForm

#Python
import datetime
import requests, pytz

from drchrono.settings import SOCIAL_AUTH_DRCHRONO_KEY, SOCIAL_AUTH_DRCHRONO_SECRET


def oauth_flow(request):
    pass
    return


def index(request):
    """Sign In"""
    return render(request, 'index.html')


def home(request):
    """Patient Check-in"""

    form = PatientForm()

    # if form.is_valid():
    #     return HttpResponseRedirect('/demographic/')

    return render(request, 'home.html', {'form': form})


def check_in(request):
    """Patient Check-in"""

    form = PatientForm()

    return render(request, 'check_in.html', {'form': form})


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
        auth_token = request.user
    except Doctor.DoesNotExist:
        auth_token = Doctor(user=request.user, access_token=access_token, refresh_token=refresh_token,
                        expires_timestamp=expires_timestamp)
        auth_token.save()

    return HttpResponseRedirect(reverse('home'))


def patient_demographic(request):
    """Patient chart that gets updated by patient on check in"""

    headers = {
        'Authorization': 'Bearer ACCESS_TOKEN',
    }

    patient_info = []
    patients_url = 'https://drchrono.com/api/patients'

    # while patients_url:
    #     data = requests.get(patients_url, headers=headers).json()
    #     patient_info.extend(data['results'])
    #     patients_url = data['next']

    return render(request, 'demographic.html')


def set_appointment_status(request):
    """Set appointment status for patient to 'Arrived'"""
    pass


def appointments(request):
    """Lists all of today's appointments."""

    return render(request, 'appointment.html')


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
