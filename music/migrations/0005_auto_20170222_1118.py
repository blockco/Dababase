# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-22 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170222_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dab',
            options={'ordering': ['-timestamp']},
        ),
    ]
