# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=5)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('interest', models.CharField(max_length=50)),
                ('autobiography', models.CharField(max_length=100)),
            ],
        ),
    ]
