from django.db import models
from register.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
        description = models.CharField(max_length=255)
        pic = models.FileField(upload_to='uploads', blank=True)
        date_posted = models.DateTimeField(default=timezone.now)
        user_name = models.ForeignKey(User, on_delete=models.CASCADE)
        tags = models.CharField(max_length=100, blank=True)
        like = models.PositiveIntegerField(default=0, null=True)
        comment = models.PositiveIntegerField(default=0, null=True)

        def __str__(self):
            return self.description

class LikePost(models.Model):
    post_id =models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Comment(models.Model):
    post= models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.description, self.name)

