# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170718_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zustellung',
            options={'ordering': ('strasse', 'hausnummer')},
        ),
    ]
