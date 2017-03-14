from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(User)

    #OAuth stored in Doctor model since it has One to One relationship with user
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    expires_timestamp = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user.username


class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    ssn = models.IntegerField()

    def __unicode__(self):
        return self.first_name

