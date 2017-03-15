# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0006_patient_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency_contact_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
