# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0015_auto_20170323_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='scheduled_time',
            field=models.DateTimeField(),
        ),
    ]
