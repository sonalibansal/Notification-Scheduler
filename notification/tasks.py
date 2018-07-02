from __future__ import absolute_import, unicode_literals

import datetime
import smtplib

from celery import Task
from django.contrib.auth.models import User

from notification.models import Notification, UserNotification
from assignment.celery import app



class NotificationScheduler(Task):

    def __init__(self):
        print "parent class"

    def run(self,user_id,notification_id):
        print(user_id)
        print("hello")
        user=User.objects.get(pk=user_id)
        notification=Notification.objects.get(pk=notification_id)
        usernotification=UserNotification.objects.get(user=user,notification=notification)
        now = datetime.datetime.now()
        subject = notification.header
        email = 'sonali@zopper.com'
        message = notification.content
        from_email = 'shareadcare@gmail.com'
        password = 'mirsajsob2017'
        sendmailobj = app.register_task(SendEmail())
        if usernotification.status=='inactive' :
            print(" INACTIVE")
            if now.date()>notification.noti_date:

                status=sendmailobj.delay(notification.header,email,from_email,notification.content,password)
                usernotification.status = status
                usernotification.save()
                print usernotification.status
            elif now.date()==notification.noti_date and now.strftime("%H:%M:%S")==notification.noti_time:
                status =sendmailobj.delay(notification.header, email, from_email, notification.content, password)
                usernotification.status = status
                usernotification.save()
                print usernotification.status
            else:
                print 'NOTIFICATION NOT SCHEDULED YET'

        elif usernotification.status=='failed':
            status = sendmailobj.delay(notification.header, email, from_email, notification.content, password)
            usernotification.status = status
            usernotification.save()
            print usernotification.status

        else:
            print "no notifications pending"

obj=app.register_task(NotificationScheduler())

class SendEmail(NotificationScheduler):

    def __init__(self):
        print "child class"


    def run(self,subject, to, sender, message, password):
        try:
            email_msg = "Subject: {} \n\n{}".format(subject, message)
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login(sender, password)
            smtp.sendmail(sender, to, email_msg)
            smtp.close()
            return 'successful'
        except Exception:

            return 'failed'

obj2=app.register_task(SendEmail())

'''
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
django.setup()
'''

