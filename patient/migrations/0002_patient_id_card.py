# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2021-01-11 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='id_card',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
