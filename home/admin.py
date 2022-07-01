from django.contrib import admin 

from .models import Post, Profile ,LikePost,FollowersCount ,Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(Comment)
