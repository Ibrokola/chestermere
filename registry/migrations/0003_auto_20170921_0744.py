# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_auto_20170919_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='regheaderimage',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='regheaderimage',
            name='intro',
            field=models.TextField(),
        ),
    ]
