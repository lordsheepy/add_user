from django.conf.urls import patterns, url
from adduser import views

urlpatterns= patterns('',
                      url(r'^$', views.index, name='index'),
                      url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
                      url(r'^addnewuser', views.addnewuser, name='addnewuser'),
                      url(r'^edituser/(?P<user_id>\d+)/$', views.edituser, name='edituser')
)