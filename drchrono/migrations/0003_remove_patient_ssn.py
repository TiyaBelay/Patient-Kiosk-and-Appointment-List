# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0002_auto_20170314_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='ssn',
        ),
    ]
