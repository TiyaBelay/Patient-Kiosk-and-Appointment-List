from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField, USSocialSecurityNumberField
from django.utils.timezone import localtime, now


class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(User)
    office = models.IntegerField(default=3456)

    #OAuth stored in Doctor model since it has One to One relationship with user
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    expires_timestamp = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username


class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=20, null=True)
    state = USStateField(max_length=2, null=True)
    zip_code = USZipCodeField(null=True)
    cell_phone = PhoneNumberField(null=True)
    email = models.CharField(max_length=40, null=True)
    emergency_contact_name = models.CharField(max_length=40, null=True)
    emergency_contact_phone = PhoneNumberField(null=True)
    emergency_contact_relation = models.CharField(max_length=20, null=True)
    ethnicity = models.CharField(max_length=20, null=True)
    preferred_language = models.CharField(max_length=20, null=True)
    race = models.CharField(max_length=20, null=True)
    social_security_number = USSocialSecurityNumberField(null=True)
    appointment_status = models.CharField(max_length=30, default="Not Arrived")
    scheduled_time = models.DateField(default=localtime(now()).date())
    duration = models.IntegerField(default=30)

    def __unicode__(self):
        return self.first_name
