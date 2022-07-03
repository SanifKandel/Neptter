from curses import use_default_colors
from pyexpat import model
from django.shortcuts import render

from .models import  Post, LikePost,Comment
from .forms import NewPostForm, NewCommentForm
from register.models import User 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context import Context

# Create your views here.

@login_required(login_url='login')
def create_post(request):
    print(request.POST.get('pic',None))
    
    user = request.user
    if request.method == "POST":
      image= request.FILES.get('pic',None)
      caption= request.POST.get('description',None)
      form = NewPostForm(request.POST, request.FILES)
      if form.is_valid():
        data = Post()
        data.user_name = user
        data.description = caption
        if image :
          data.pic = image
        data.save()
       
        messages.success(request, f'Posted Successfully')
        return redirect('home')
    else:
      
      form = NewPostForm(request.POST, request.FILES)
      return render(request, 'home', {'form':form})

@login_required(login_url='login')
def Postdelete(request,post_id): 
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')

@login_required(login_url='login')
def Postlike (request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)
    like_filter = LikePost.objects.filter(post_id=post_id,username=username).first()
    like_filters = LikePost.objects.filter(post_id=post_id,username=username)
    print(like_filters)

    if like_filter == None:
        new_like =LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.like = post.like+1
        post.save()
        
       

    else:
        like_filter.delete()
        post.like = post.like-1
        post.save()
    
    context={
        'like_filters' :like_filters,
    
    }  
  
    return redirect('/',context)


@login_required
def Postcomment(request,pk):
    user =request.user
    post =Post.objects.all()
    user_posts =Post.objects.filter(id=pk)
    comments = Comment.objects.filter(post_id=pk)
    post_id = pk

    context={
        'posts': user_posts,
        'comments': comments,
        'post_id': post_id,
        'user':user
    }
    return render(request, 'comment.html',context)



@login_required
def create_comment(request,pk):
    user =request.user.username 
    print(user)
    current_user =User.objects.get(username=user)
    print(current_user)
  
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        comment = request.POST.get('body',None)
        print(comment)
        form = NewCommentForm(request.POST)
        if  form.is_valid():
            data =  Comment()
            data.name = current_user.first_name
            data.post = post
            data.body = comment
            data.save()
            print("form saved")
            return redirect('comment',pk)
            
        else:
            form = NewCommentForm(request.POST)
            return render(request, 'comment', pk,{'form':form})

@login_required
def Commentdelete(request,comment_id): 
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('comment')