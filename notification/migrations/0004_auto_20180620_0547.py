# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_usernotification_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='date',
            new_name='noti_date',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='time',
            new_name='noti_time',
        ),
    ]
