# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0004_auto_20170921_0751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='title1',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='section',
            name='title2',
        ),
    ]
