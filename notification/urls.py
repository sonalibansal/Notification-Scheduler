from django.conf.urls import include,url

from . import views

urlpatterns = [
   
    #url(r'^notification/$',views.noti,name='noti'),
    url(r'^notifications/$', views.NotificationList.as_view()),
    url(r'^notifications/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view()),
    url(r'^usernotifications/$', views.UserNotificationList.as_view()),

    url(r'^users/$', views.UsersList.as_view()),

    #url(r'^notification/$', views.notification_list),


]	