from django.urls import path
from . import views

urlpatterns = [
    path('admins/', views.admin_dashboard, name='admin_dashboard'),

]