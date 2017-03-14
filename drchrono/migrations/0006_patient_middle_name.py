# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0005_auto_20170314_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
