# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.TextField(default='Hello', max_length=3000),
        ),
    ]
