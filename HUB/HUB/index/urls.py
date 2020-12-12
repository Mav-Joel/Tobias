from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<slot>[0-1])/$',views.getSlotFromDb),
    url(r'^search/$', views.search),
]