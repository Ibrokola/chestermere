# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20170920_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAdImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutAdTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='AboutAd',
        ),
        migrations.AddField(
            model_name='aboutadimage',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.AboutAdTitle'),
        ),
    ]