from django.contrib.auth.models import User
from django.db import models




# Create your models here.
class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.IntegerField()

    def __str__(self):
        return self.user.username