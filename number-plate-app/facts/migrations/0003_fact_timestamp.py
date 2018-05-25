# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0002_auto_20180525_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
