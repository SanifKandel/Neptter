from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    gender = (
        ('M','Male'),
        ('F', 'Female'),
        ('O','Others'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=300, null=True)
    profile_pic = models.FileField(upload_to='uploads', default='user.png')
    birthday = models.DateField(auto_now_add=False, null=True)
    gender = models.CharField(max_length=2, choices=gender, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username