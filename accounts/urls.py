from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = "accounts"

urlpatterns = [

    url(r'^register', views.register, name='register'),
    url(r'^login', views.signin, name='login'),
    url(r'^logout', views.signout, name='logout'),

]
