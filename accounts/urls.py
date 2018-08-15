from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = "accounts"

urlpatterns = [

    url(r'^register/index$', views.index, name='register_index'),
    url(r'^register/create$', views.create, name='register_create'),

]
