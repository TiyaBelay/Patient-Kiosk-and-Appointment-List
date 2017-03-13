# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('access_token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
                ('expires_timestamp', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('ssn', models.IntegerField()),
            ],
        ),
    ]
