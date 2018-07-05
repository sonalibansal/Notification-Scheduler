import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
# django.setup()
from assignment.celery import app
from notification.tasks import  NotificationScheduler
from notification.models import UserNotification

usernotifications=UserNotification.objects.all()
for usernotification in usernotifications:

    print("user id "+str(usernotification.user.id)+" notification id "+str(usernotification.notification.id))
    object = app.register_task(NotificationScheduler())
    r=object.apply_async(countdown=5,args=[usernotification.user.id,usernotification.notification.id])
    print r.state





