from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [


 path('',views.HomeProcess.as_view(),name="home"),
 path('profile/',views.ProfileProcess,name="profile"),
  path('myprofile/',views.MyProfile.as_view(),name="myprofile"),
 path('aboutus/',views.AboutProcess,name="about"),
 path('post/',views.create_post,name="post"),
 path('deletepost/',views.Postdelete,name="postdelete"),
  path('likepost/',views.Postlike,name="likepost"),
]