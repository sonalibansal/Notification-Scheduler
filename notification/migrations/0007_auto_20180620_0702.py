# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_auto_20180620_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='noti_time',
            field=models.TimeField(),
        ),
    ]