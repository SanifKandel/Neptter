from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from login import views

urlpatterns = [

    path('login/',views.loginProcess,name="login"),
    # path('forgetpassword/',views.ForgetPass,name="forget"),
    # path('resetpassword/<token>/',views.resetPassword,name="reset"),

    path('reset-password-enterusername', views.entermailResetpassword, name='reset-password-enterusername'),
    path('reset-password/<token>/', views.resetPassword, name='reset-password'),
    path('reset-password-done', views.resetpasswordDone, name='reset-password-done'),

   
]