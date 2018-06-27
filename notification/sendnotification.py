from . import UserNotification,Notification
from django.contrib.auth.models import User

def notification_status(user_id,notification_id):
    user=User.objects.get(pk=user_id)
    notification=Notification.objects.get(pk=notification_id)
    usernotification=UserNotification.objects.get(user=user,notification=notification)
    if(usernotification.status=='inactive'):
        print(usernotification.status)



notification_status(4,2)
