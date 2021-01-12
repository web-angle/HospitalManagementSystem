# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2021-01-11 09:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=25, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField(blank=True, default=20, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('C+', 'C+'), ('C-', 'C-'), ('O+', 'O+'), ('O-', 'O-')], max_length=2, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='patients')),
                ('diseases', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('patient_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]