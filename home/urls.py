from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [


 path('',views.HomeProcess.as_view(),name="home"),
 path('profile/',views.ProfileProcess,name="profile"),
 path('aboutus/',views.AboutProcess,name="about"),
 path('post/',views.create_post,name="post"),
]