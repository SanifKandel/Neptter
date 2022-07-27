from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
 path('aboutus/',views.AboutProcess,name="about"),
 path('profile/',views.ProfileProcess,name="profile"),
 path('',views.HomeProcess,name="home"),
 



]
