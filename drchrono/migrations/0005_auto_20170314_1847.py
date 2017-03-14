# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0004_auto_20170314_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='cell_phone',
            field=localflavor.us.models.PhoneNumberField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emergency_contact_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emergency_contact_phone',
            field=localflavor.us.models.PhoneNumberField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emergency_contact_relation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='ethnicity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='preferred_language',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='race',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='social_security_number',
            field=localflavor.us.models.USSocialSecurityNumberField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='zip_code',
            field=localflavor.us.models.USPostalCodeField(max_length=2, null=True),
        ),
    ]
