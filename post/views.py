from itertools import chain
import random
from django.http import JsonResponse
from django.shortcuts import render

from .models import  Post, LikePost,Comment
from userprofile.models import  Profile , FollowerCount
from .forms import NewPostForm, NewCommentForm
from register.models import User 
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages


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

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required(login_url='login')
def Postlike (request):
    if is_ajax(request=request):
        print("inside ajax")
        username = request.user.username
        post_id = request.POST.get('post_id')

        post = Post.objects.get(id=post_id)
        like_filter = LikePost.objects.filter(post_id=post_id,username=username).first()
        like_filters = LikePost.objects.filter(post_id=post_id,username=username)
        print(like_filters)
        status = False
        

        if like_filter == None:
            new_like =LikePost.objects.create(post_id=post_id, username=username)
            status = True
            new_like.save()
            post.like = post.like+1
            post.save()
            
        

        else:
            like_filter.delete()
            status= False
            post.like = post.like-1
            post.save()
        
        context={
            'like_filters' :like_filters,
        
        }  
    
        return JsonResponse(status,safe=False)



@login_required
def Postcomment(request,pk):
    userd =request.user
    post =Post.objects.all()
    user_posts =Post.objects.filter(id=pk)
    comments = Comment.objects.filter(post_id=pk)
    post_id = pk
    all_users = User.objects.all()
    user_following = FollowerCount.objects.filter(follower=request.user.username)


    # Friends Suggestions
    user_following_all =[]

    for user in user_following:
        user_list =User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(user_id=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    user_comments =Comment.objects.filter(post=pk)
    user_comment_length = len(user_comments)

   
    context={
        'posts': user_posts,
        'comments': comments,
        'post_id': post_id,
        'user': userd,
        'user_comment_length':user_comment_length,
        'suggestions_username_profile_list':suggestions_username_profile_list[:4]
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
            data.user= current_user
            data.post = post
            data.body = comment
            data.save()
            post.comment = post.comment + 1
            post.save()
            print("form saved")
            return redirect('comment',pk)
            
        else:
            form = NewCommentForm(request.POST)
            return render(request, 'comment', pk,{'form':form})

@login_required
def Commentdelete(request,comment_id): 
    comment = Comment.objects.get(id=comment_id)
    commentid = comment.post.id
    post=Post.objects.get(id=commentid)
    post.comment = post.comment - 1
    post.save()

    comment.delete()
    return redirect('comment',commentid)