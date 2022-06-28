from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [


 path('',login_required(views.HomeProcess.as_view()),name="home"),
 path('profile/',views.ProfileProcess,name="profile"),
#  path('myprofile/',login_required(views.MyProfile.as_view()),name="myprofile"),
 path('profile/<str:pk>',views.MyProfiles,name="myprofiles"),
 path('aboutus/',views.AboutProcess,name="about"),
 path('post/',views.create_post,name="post"),
 path('deletepost/',views.Postdelete,name="postdelete"),
  path('likepost/',views.Postlike,name="likepost"),
]