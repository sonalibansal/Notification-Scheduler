from django.contrib.auth.models import User
from .models import Notification,UserNotification
from rest_framework import serializers
from rest_framework.response import Response


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('id','username')

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



	def create(self,validated_data):
		user_data=validated_data.pop('user')
		notification=Notification.objects.create(validated_data)


		user_data=validated_data.pop('user')
		notification = Notification.objects.create(**validated_data)
		UserNotification.objects.create(notification=notification,**user_data)
		return notification


		user=UserSerializer.create(data=user_data,many=True)

		notification= UserNotification.objects.create(user=user,notification=notification,status='inactive')
		return student


		user = UserSerializer.create(UserSerializer(), validated_data=user_data)
		UserNotification.objects.create(notification=notification, **user_data)
		return notification







class UserNotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserNotification
		fields=('user','notification','status')
		#fields = ('user', 'notification','status')





'''