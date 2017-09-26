# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20170922_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='external_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]