# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional', '0002_calender_daysclosed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daysclosed',
            name='days',
            field=models.TextField(blank=True, null=True),
        ),
    ]
