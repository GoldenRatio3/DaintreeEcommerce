# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20170315_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
