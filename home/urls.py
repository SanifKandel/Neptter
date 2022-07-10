from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
 path('',views.HomeProcess,name="home"),
 path('aboutus/',views.AboutProcess,name="about"),
]
