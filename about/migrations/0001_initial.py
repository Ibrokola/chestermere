# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.TextField(default='Hello', max_length=3000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'about',
            },
        ),
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
        migrations.CreateModel(
            name='AboutHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='aboutadimage',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.AboutAdTitle'),
        ),
    ]
