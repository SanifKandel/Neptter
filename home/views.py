import random
from django.shortcuts import render
from post.models import Post
from userprofile.models import Profile ,FollowerCount
from register.models import User 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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


def AboutProcess(request):
    return render(request, 'aboutus.html')
