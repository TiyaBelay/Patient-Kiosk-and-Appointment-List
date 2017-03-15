# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0007_auto_20170315_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='appointment_status',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
