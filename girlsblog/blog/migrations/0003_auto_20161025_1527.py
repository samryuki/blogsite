# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-25 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161025_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_on_date',
            new_name='created_date',
        ),
    ]
