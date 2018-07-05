# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Notification(models.Model):
	header=models.CharField(max_length=50)
	content=models.CharField(max_length=500)
	image=models.CharField(max_length=200)
	noti_date=models.DateField()
	noti_time=models.TimeField ()



class UserNotification(models.Model):

	user=models.ForeignKey(User)
	notification=models.ForeignKey(Notification)
	status=models.CharField(max_length=12,default='inactive')




