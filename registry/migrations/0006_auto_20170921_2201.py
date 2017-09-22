# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0005_auto_20170921_0753'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegHeaderImage',
        ),
        migrations.RemoveField(
            model_name='regform',
            name='download_file',
        ),
        migrations.AddField(
            model_name='regform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='regform',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regform',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]