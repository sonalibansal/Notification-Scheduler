# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import status,permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from notification.models import Notification,UserNotification
from notification.serializers import NotificationSerializer,UserNotificationSerializer,UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from django.contrib.auth.models import User

from rest_framework import status
from django.http import HttpResponse
import pprint

class UsersList(APIView):

    def get(self,request,format=None):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)



class NotificationList(APIView):
    
    def get(self, request, format=None):
       	notifications = Notification.objects.all()
    	r=[]
		
    	for n in  notifications:
    		serializer=NotificationSerializer(n)
    		r.append(serializer.data)
    	return Response(r)


    def post(self, request, format=None):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationDetail(APIView):
    """
    Retrieve, update or delete a notification instance.
    """
    def get_object(self, pk):
        try:
            return Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        notification = self.get_object(pk)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        notification = self.get_object(pk)
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        notification = self.get_object(pk)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserNotificationList(APIView):
    """
    List all notifications, or create a new notification.
    """

    def get(self, request, format=None):
        usernotifications=UserNotification.objects.all()
        usernotificationserializer=UserNotificationSerializer(usernotifications,many=True)
        return Response(usernotificationserializer.data)
    



    def post(self, request, format=None):
        serializer = UserNotificationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

