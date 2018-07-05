from .models import Notification,UserNotification
from rest_framework import serializers
from django.contrib.auth.models import User

from notification.tasks import SendEmail

class UserSerializer(serializers.ModelSerializer):
	username = serializers.ReadOnlyField(source='user.username')
	class Meta:
		model=UserNotification
		fields=('id','username')


class NotificationSerializer(serializers.ModelSerializer):
	user=UserSerializer(many=True, source="usernotification_set")
	class Meta:
		model=Notification
		fields=('id','header','content','image','noti_date','noti_time','user')

	def create(self, validated_data):
		user_data=validated_data.pop('user')
		notification=super(NotificationSerializer,self).create(validated_data)
		for u in user_data:
			user=User.objects.get(pk=u['id'])
			usernotification=UserNotification.objects.create(notification=notification,user=user)
			object=SendEmail()
			object.notification_status(usernotification.user.id,usernotification.notification.id)

		return notification

class UserNotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserNotification
		fields=('user','notification','status')
