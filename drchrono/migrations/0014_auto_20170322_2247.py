# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0013_auto_20170322_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(max_length=10, null=True),
        ),
    ]
