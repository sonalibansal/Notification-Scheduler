# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 04:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_auto_20180621_0506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usernotification',
            old_name='notification_id',
            new_name='notification',
        ),
        migrations.RenameField(
            model_name='usernotification',
            old_name='user_id',
            new_name='user',
        ),
    ]
