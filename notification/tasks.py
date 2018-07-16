from __future__ import absolute_import, unicode_literals

import datetime
import smtplib

from celery import Task
from django.contrib.auth.models import User

from assignment.settings import *
from notification.models import Notification, UserNotification
from assignment.celery import app



def time_in_seconds(d1,t1):
    now = datetime.datetime.now()
    current_date=now.date()
    timedelta=d1-current_date
    return timedelta.days*24*3600+now.time().second-t1.second

class NotificationScheduler(Task):

    def __init__(self):
        print "parent class"

    def notification_status(self,user_id,notification_id):

        user=User.objects.get(pk=user_id)
        notification=Notification.objects.get(pk=notification_id)
        usernotification=UserNotification.objects.get(user=user,notification=notification)
        subject = notification.header
        email = user.email
        message = notification.content
        from_email = EMAIL_HOST
        password = EMAIL_PASSWORD
        sendmailobj = app.register_task(SendEmail())
        seconds=time_in_seconds(notification.noti_date,notification.noti_time)
        sendmailobj.apply_async(countdown=seconds,args=[subject,email,from_email,message,password])

class SendEmail(NotificationScheduler):

    def __init__(self):
        print "child class"


    def run(self,*args):

        try:
            email_msg = "Subject: {} \n\n{}".format(args[0], args[3])
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login(args[2], args[4])
            smtp.sendmail(args[2], args[1], email_msg)

            smtp.close()
            return 'SUCCESSFUL'
        except Exception:

            return 'FAILED'

obj=app.register_task(SendEmail())


