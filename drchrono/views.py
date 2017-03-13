#Django
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from models import Doctor

#Python
import datetime
import requests, pytz

from drchrono.settings import SOCIAL_AUTH_DRCHRONO_KEY, SOCIAL_AUTH_DRCHRONO_SECRET


def index(request):
    """Sign In"""
    return render(request, 'index.html')


def home(request):
    """Patient Check-in"""
    return render(request, 'home.html')


def drchrono_login(request):
    print request
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


def drchrono_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
