from django.contrib import admin 

from .models import Post ,LikePost,Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(LikePost)

admin.site.register(Comment)
