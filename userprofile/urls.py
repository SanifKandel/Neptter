from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
 path('follow/',views.Follow,name="follow"),
 path('profile/<str:pk>',views.MyProfiles,name="myprofiles"),
]