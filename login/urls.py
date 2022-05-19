from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    path('login/',views.loginProcess,name="login"),
    path('index/',views.HomeProcess,name="index"),
    path('forgetpassword/',views.ForgetPass,name="forget"),


   
]