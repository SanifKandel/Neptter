from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from home.models import Post, LikePost
from register.models import User
from django.shortcuts import render, redirect

# Create your views here.
from login.auth import admin_only




@login_required
@admin_only
def admin_dashboard(request):
    user = User.objects.filter(is_staff=0)
    user_count = user.count()
    admin = User.objects.filter(is_staff=1)
    admin_count = admin.count()
    user_info = user.filter(is_staff=0)
    admin_info = admin

    post = Post.objects.all()
    post_count = post.count()
    like = LikePost.objects.all()
    like_count = like.count()

    print(admin_info)

    context = {
        'user': user_count,
        'admins': admin_count,
        'user_info': user_info,
        'admin_info': admin_info,
        'post': post_count,
        'like': like_count,
    }
    return render(request, 'admin-dashboard.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

