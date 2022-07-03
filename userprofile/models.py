from django.db import models
from register.models import User

# Create your models here.
class Profile(models.Model):

    gender = (
        ('M','Male'),
        ('F', 'Female'),
        ('O','Others'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=300, null=True)
    profile_pic = models.FileField(upload_to='uploads', default='man.png')
    cover_pic = models.FileField(upload_to='uploads', default='democover.png')
    bio = models.CharField(max_length=255,blank=True ,default='')
    birthday = models.DateField(auto_now_add=False, null=True)
    gender = models.CharField(max_length=2, choices=gender, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

class FollowerCount(models.Model):
    user_id = models.CharField(max_length=500,null=True)
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

