import math
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

        def whenpublished(self):
            now = timezone.now()
            
            diff= now - self.date_posted

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

                

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days= diff.days
            
                if days == 1:
                    return str(days) + " day ago"

                else:
                    return str(days) + " days ago"

            if diff.days >= 30 and diff.days < 365:
                months= math.floor(diff.days/30)
                

                if months == 1:
                    return str(months) + " month ago"

                else:
                    return str(months) + " months ago"


            if diff.days >= 365:
                years= math.floor(diff.days/365)

                if years == 1:
                    return str(years) + " year ago"

                else:
                    return str(years) + " years ago"

class LikePost(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE)
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

