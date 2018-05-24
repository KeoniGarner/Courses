from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.courses),
    re_path(r'^courses/$', views.index, name="home"),
    re_path(r'^courses/create/$', views.create, name="create"),
    re_path(r'^courses/destroy/(?P<id>\d+)/$', views.confirm, name="confirm"),
    re_path(r'^courses/destroy/(?P<id>\d+)/confirmed/$', views.destroy, name="destroy"),
]