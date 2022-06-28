from pyexpat import model
from django.shortcuts import render

from .models import Profile , Post, LikePost,FollowersCount
from .forms import ProfileForm, NewPostForm
from register.models import User 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context import Context

# Create your views here.

# class HomeProcess(ListView):
#   model = Post
#   template_name = 'home.html'
#   context_object_name = 'posts'


#   def get_context_data(self, **kwargs):
#    context = super(HomeProcess, self).get_context_data(**kwargs)
#    return context

def HomeProcess(request):
    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)
    user_posts =Post.objects.all()

    user_following_list =[]
    feed =[]

    

    context={
    'user_object':user_object,
    'user_profile': user_profile,
    'user_posts':user_posts,
    }
    
    return render(request, 'home.html',context)

class MyProfile(ListView):
  http_method_names=['post','get']
  model = Post
  template_name = 'profileupdate.html'
  context_object_name = 'posts'

  def post(self, request, **kwargs):  
    cuser = request.user.profile
    if request.method == 'POST':
        profile = ProfileForm(request.POST, request.FILES, instance=cuser)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        if profile.is_valid():
            User.objects.filter(username=cuser).update(
                first_name=full_name, email=email, username=username)
            profile.save()
        else:
            context = {'profile': profile}
            return render(request, 'profileupdate.html', context)

    context = {
        'profile':ProfileForm(instance=cuser),
        'post':'model',
    }

    return render(request, 'profileupdate.html',context)

        
  def get_context_data(self, **kwargs):
   context = super(MyProfile, self).get_context_data(**kwargs)
   form = ProfileForm(initial={
    'phone':self.request.user.profile.phone,
    'address':self.request.user.profile.address,
    'bio':self.request.user.profile.bio,
    'gender':self.request.user.profile.gender,
    'birthday':self.request.user.profile.birthday,
    'cover_pic':self.request.user.profile.cover_pic.name,
    'profile_pic':self.request.user.profile.profile_pic,

   })
   context['profile']=form
   context['rtn']=True
   return context



@login_required(login_url='login')
def ProfileProcess(request):
    rtn = request.POST.get('rtn', None)
    cuser = request.user.profile
    if request.method == 'POST':
        profile = ProfileForm(request.POST, request.FILES, instance=cuser)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        if profile.is_valid():
            User.objects.filter(username=cuser).update(
                first_name=full_name, email=email, username=username)
            profile.save()
        else:

            context = {'profile': profile}
            if rtn:
                return redirect('myprofile')
            return render(request, 'profile.html', context)

    context = {
        'profile':ProfileForm(instance=cuser),
    }
    if rtn:
                return redirect('myprofile')
    return render(request, 'profile.html',context)


@login_required(login_url='login')
def create_post(request):
    print(request.POST.get('pic',None))
    
    user = request.user
    if request.method == "POST":
      image= request.FILES.get('pic',None)
      caption= request.POST.get('description',None)
      form = NewPostForm(request.POST, request.FILES)
      if form.is_valid():
      
        # data = form.save(commit=False)
        data = Post()
        # print(Post.pic.content_type()) 
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
def Postdelete(request):
    post = Post.objects.get(id=request.POST.get('id'))
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
        user_object = User.objects.get(username=pk)
        user_profile = Profile.objects.get(user=user_object)
        user_posts =Post.objects.filter(user_name=user_object)
        user_post_length = len(user_posts)
        follower = request.user.username
        user = pk
        button_check="unfollow"

        if FollowersCount.objects.filter(follower=follower ,user=user).first():
            button_text = "unfollow"
        else:
            button_text = "Follow"

        followers =len(FollowersCount.objects.filter(user=pk))
        following =len(FollowersCount.objects.filter(follower=pk))


        form = ProfileForm(initial={
        'phone':request.user.profile.phone,
        'address':request.user.profile.address,
        'bio':request.user.profile.bio,
        'gender':request.user.profile.gender,
        'birthday':request.user.profile.birthday,
        'cover_pic':request.user.profile.cover_pic.name,
        'profile_pic':request.user.profile.profile_pic,

        })

        context={
        'profile':form,
        'user_object':user_object,
        'user_profile': user_profile,
        'user_posts':user_posts,
        'user_post_length':user_post_length,
        'pk':pk,
        'button_text':button_text,
        'button_check':button_check,
        'followers' :followers,
        'following' :following,

        }
        
        return render(request, 'profileupdate.html',context)


@login_required
def Follow(request):
    if request.method =='POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower ,user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower ,user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return render('/')