# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170718_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zusatzinformation',
            name='zustellung',
        ),
        migrations.AddField(
            model_name='zusatzinformation',
            name='zustellung',
            field=models.ManyToManyField(to='website.Zustellung'),
        ),
    ]