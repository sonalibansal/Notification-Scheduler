import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
django.setup()
from assignment.celery import app
from notification.tasks import  NotificationScheduler
object = app.register_task(NotificationScheduler())
object.delay(2,6)

