# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0003_auto_20170923_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='certcategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
