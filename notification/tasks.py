from __future__ import absolute_import, unicode_literals

import datetime
import smtplib

from celery import Task
from django.contrib.auth.models import User

from assignment.settings import *
from notification.models import Notification, UserNotification
from assignment.celery import app

class NotificationScheduler(Task):

    def __init__(self):
        print "parent class"

    def notification_status(self,user_id,notification_id):

        user=User.objects.get(pk=user_id)
        notification=Notification.objects.get(pk=notification_id)
        usernotification=UserNotification.objects.get(user=user,notification=notification)
        now = datetime.datetime.now()
        subject = notification.header
        email = user.email
        message = notification.content
        from_email = EMAIL_HOST
        print from_email
        password = EMAIL_PASSWORD
        sendmailobj = app.register_task(SendEmail())
        if usernotification.status=='inactive' :

            if now.date()>notification.noti_date:
                mail=sendmailobj.apply_async(countdown=3,args=[subject,email,from_email,message,password])
                usernotification.status=mail
                usernotification.save()
                print usernotification.status
            elif now.date()==notification.noti_date and now.strftime("%H:%M:%S")>=notification.noti_time.strftime("%H:%M:%S"):
                mail=sendmailobj.apply_async(countdown=3,args=[subject,email,from_email,message,password])
                print mail
                usernotification.status = mail
                usernotification.save()
            else:
                print 'NOTIFICATION NOT SCHEDULED YET'

        elif usernotification.status=='FAILED':
            mail = sendmailobj.apply_async(countdown=3, args=[subject, email, from_email, message, password])
            print mail
            usernotification.status = mail
            usernotification.save()

        else:
            print "notification already sent successfully"



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


