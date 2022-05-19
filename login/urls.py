from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from login import views

urlpatterns = [

    path('login/',views.loginProcess,name="login"),
    path('forgetpassword/',views.ForgetPass,name="forget"),
    path('resetpassword/',views.resetpass,name="reset"),


   
]