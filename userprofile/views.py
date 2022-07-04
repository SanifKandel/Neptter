
# Create your views here.
import random
from django.shortcuts import render

from .models import Profile ,FollowerCount
from post.models import Post
from .forms import ProfileForm 
from register.models import User 

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.template.context import Context
from itertools import chain

# Create your views here.


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
