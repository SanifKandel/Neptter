from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

# Create your models here.
class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.IntegerField()

    def __str__(self):
        return self.user.username