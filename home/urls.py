from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
 path('',views.HomeProcess,name="home"),
 path('aboutus/',views.AboutProcess,name="about"),
]