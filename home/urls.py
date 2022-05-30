from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [


 path('home/',views.HomeProcess,name="home"),
 path('profile/',views.ProfileProcess,name="profile"),
]