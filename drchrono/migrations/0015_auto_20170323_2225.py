# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0014_auto_20170322_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='arrived_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='seen_by_doc',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='scheduled_time',
            field=models.DateField(default=datetime.date(2017, 3, 23)),
        ),
    ]
