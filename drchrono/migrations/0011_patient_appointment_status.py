# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0010_remove_patient_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='appointment_status',
            field=models.CharField(default=b'Not Arrived', max_length=30),
        ),
    ]
