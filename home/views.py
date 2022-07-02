from curses import use_default_colors
from pyexpat import model
import random
from django.shortcuts import render

from .models import Profile , Post, LikePost,FollowerCount,Comment
from .forms import ProfileForm, NewPostForm, NewCommentForm
from register.models import User 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context import Context
from itertools import chain

# Create your views here.

@login_required
def HomeProcess(request):
    post =Post.objects.all()
    all_users = User.objects.all()
    user_following = FollowerCount.objects.filter(follower=request.user.username)

    #Customized Home
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list =[]
    feed =[]

    user_following = FollowerCount.objects.filter(follower=request.user.username)
    print(user_following)

    for user in user_following:
        user_list =User.objects.get(username=user.user)
        user_following_list.append(user_list)
        print(user_following_list)

    for usernames in user_following_list:
        feed_lists =Post.objects.filter(user_name_id= usernames)
        print("Before")
        print(feed_lists)
        feed.append(feed_lists)

    feed_lists =Post.objects.filter(user_name_id=user_object.id)
    feed.append(feed_lists)
    print("After")
    print(feed_lists)

    feed_list = list(chain(*feed))


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

    # comment = Comment.objects.all()
    # user_object = User.objects.get(username=comment.name)
    # posts =Post.objects.filter(user_name=user_object)
    # user_comments =Comment.objects.filter(id=posts.id)
    # user_comment_length = len(user_comments)


    context={
        'posts':post,
        'user_profile': user_profile,
        'user_posts':feed_list,
        'suggestions_username_profile_list': suggestions_username_profile_list[:4]

    }
    return render(request, 'home.html',context)

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

    if like_filter == None:
        new_like =LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.like = post.like+1
        post.save()
        liked = True
        context={
        'liked': liked
    }   

    else:
        like_filter.delete()
        post.like = post.like-1
        post.save()
        liked = False
        context={
        'liked': liked
    }
      
    return redirect('/',context)


def AboutProcess(request):
    return render(request, 'aboutus.html')

@login_required
def MyProfiles(request, pk):
    if request.method == "GET":
        all_users = User.objects.all()
        user_object = User.objects.get(username=pk)
        user_profile = Profile.objects.get(user=user_object)
        user_posts =Post.objects.filter(user_name=user_object)
        user_post_length = len(user_posts)
        follower = request.user.username
        user = pk
        button_check="unfollow"

        if FollowerCount.objects.filter(follower=follower ,user=user).first():
            button_text = "unfollow"
        else:
            button_text = "Follow"

        followers =len(FollowerCount.objects.filter(user=pk))
        following =len(FollowerCount.objects.filter(follower=pk))
    # Friends Suggestions
        user_following = FollowerCount.objects.filter(follower=request.user.username)
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



        form = ProfileForm(initial={
        'phone':request.user.profile.phone,
        'address':request.user.profile.address,
        'bio':request.user.profile.bio,
        'gender':request.user.profile.gender,
        'birthday':request.user.profile.birthday,
        'cover_pic':request.user.profile.cover_pic,
        'profile_pic':request.user.profile.profile_pic,

        })

        context={
        'profile':form,
        'user_object':user_object,
        'user_profile': user_profile,
        'user_posts':user_posts,
        'user_post_length':user_post_length,
        'suggestions_username_profile_list':suggestions_username_profile_list[:4],
        'pk':pk,
        'button_text':button_text,
        'button_check':button_check,
        'followers' :followers,
        'following' :following,

        }
        
        return render(request, 'profileupdate.html',context)

    elif request.method == "POST":
        cuser = request.user.profile
        profile = ProfileForm(request.POST, request.FILES, instance=cuser)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pk =username
        if profile.is_valid():
            User.objects.filter(username=cuser).update(
                first_name=full_name, email=email, username=username)
            profile.save()
        return redirect('myprofiles' ,pk)



@login_required
def Follow(request):
    if request.method =='POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowerCount.objects.filter(follower=follower ,user=user).first():
            delete_follower = FollowerCount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowerCount.objects.create(follower=follower ,user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return render('/')

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