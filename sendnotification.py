import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
django.setup()
from assignment.celery import app
from notification.tasks import  NotificationScheduler
from notification.models import UserNotification
object = app.register_task(NotificationScheduler())

usernotifications=UserNotification.objects.all()
for usernotification in usernotifications:
    object.delay(usernotification.user.id,usernotification.notification.id)
#object.delay(2,6)

