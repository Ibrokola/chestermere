# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homeintro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeintro',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
