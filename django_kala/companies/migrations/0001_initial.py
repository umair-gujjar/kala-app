# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 06:02
from __future__ import unicode_literals

from django.db import migrations, models
import django_localflavor_us.models
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=80, null=True)),
                ('zip', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, default='US', max_length=80, null=True)),
                ('fax', django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20, null=True)),
                ('phone', django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20, null=True)),
                ('locale', models.CharField(blank=True, default='en', max_length=2, null=True)),
                ('removed', models.DateField(null=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default='UTC')),
                ('website', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'kala_companies',
                'ordering': ['name'],
            },
        ),
    ]
