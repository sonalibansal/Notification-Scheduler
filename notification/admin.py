
from django.contrib import admin
from django.db import models
from .models import Notification,UserNotification
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Notification)
admin.site.register(UserNotification)
