# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0011_patient_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='office',
            field=models.IntegerField(default=345678),
        ),
        migrations.AddField(
            model_name='patient',
            name='duration',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='patient',
            name='scheduled_time',
            field=models.DateField(default=datetime.date(2017, 3, 15)),
        ),
    ]
