from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
 path('post/',views.create_post,name="post"),
 path('deletepost/<int:post_id>',views.Postdelete,name="postdelete"),
 path('comment/<int:pk>',views.Postcomment,name="comment"),
 path('createcomment/<int:pk>',views.create_comment,name="createcomment"),
 path('deletecomment/<int:comment_id>',views.Commentdelete,name="deletecomment"),
]