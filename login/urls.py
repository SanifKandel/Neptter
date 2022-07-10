from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    path('login/',views.loginProcess,name="login"),
    path('logout_user/',views.logoutUser,name="logout"),
    path('reset-password-enterusername', views.entermailResetpassword, name='reset-password-enterusername'),
    path('reset-password/<token>/', views.resetPassword, name='reset-password'),
    path('reset-password-done', views.resetpasswordDone, name='reset-password-done'),

   
]