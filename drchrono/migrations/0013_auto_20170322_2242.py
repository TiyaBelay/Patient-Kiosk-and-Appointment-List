# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0012_auto_20170315_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='office',
            field=models.IntegerField(default=3456),
        ),
        migrations.AlterField(
            model_name='patient',
            name='scheduled_time',
            field=models.DateField(default=datetime.date(2017, 3, 22)),
        ),
    ]
