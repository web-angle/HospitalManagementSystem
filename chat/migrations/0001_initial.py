# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2021-01-11 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_patient', models.TextField(blank=True, null=True)),
                ('msg_doctor', models.TextField(blank=True, null=True)),
                ('display', models.BooleanField(default=True)),
                ('from_patient', models.BooleanField(default=False)),
                ('from_doctor', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
    ]
