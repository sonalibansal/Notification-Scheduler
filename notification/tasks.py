from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime
from notification.models import Notification,UserNotification
from django.contrib.auth.models import User
import smtplib
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
django.setup()

@shared_task()

class NotificationScheduler:

    def __init__(self):
        print "parent class"

    def notification_status(self,user_id,notification_id):
        user=User.objects.get(pk=user_id)
        notification=Notification.objects.get(pk=notification_id)
        usernotification=UserNotification.objects.get(user=user,notification=notification)
        now = datetime.datetime.now()
        subject = notification.header
        email = 'sonali@zopper.com'
        message = notification.content
        from_email = 'shareadcare@gmail.com'
        password = 'mirsajsob2017'
        sendmailobj=SendEmail()
        if usernotification.status=='inactive' :
            print(" INACTIVE")
            if now.date()>notification.noti_date:

                status=sendmailobj.send_mail(notification.header,email,from_email,notification.content,password)
                usernotification.status = status
                usernotification.save()
                print usernotification.status
            elif now.date()==notification.noti_date and now.strftime("%H:%M:%S")==notification.noti_time:
                status =sendmailobj.send_mail(notification.header, email, from_email, notification.content, password)
                usernotification.status = status
                usernotification.save()
                print usernotification.status
            else:
                print 'NOTIFICATION NOT SCHEDULED YET'

        elif usernotification.status=='failed':
            status = sendmailobj.send_mail(notification.header, email, from_email, notification.content, password)
            usernotification.status = status
            usernotification.save()
            print usernotification.status

        else:
            print "no notifications pending"


@shared_task()
class SendEmail(NotificationScheduler):

    def __init__(self):
        print "child class"

    def send_mail(self,subject, to, sender, message, password):
        try:
            email_msg = "Subject: {} \n\n{}".format(subject, message)
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login(sender, password)
            smtp.sendmail(sender, to, email_msg)
            smtp.close()
            return 'successful'
        except Exception:

            return 'failed'

