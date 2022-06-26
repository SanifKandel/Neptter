from django.shortcuts import render

from .models import Profile , Post, LikePost
from .forms import ProfileForm, NewPostForm
from register.models import User 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context import Context

# Create your views here.

class HomeProcess(ListView):
  model = Post
  template_name = 'home.html'
  context_object_name = 'posts'


  def get_context_data(self, **kwargs):
   context = super(HomeProcess, self).get_context_data(**kwargs)
   return context



@login_required
def ProfileProcess(request):
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
            return render(request, 'profile.html', context)


    context = {
        'profile':ProfileForm(instance=cuser),
    }
    return render(request, 'profile.html',context)


@login_required
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

@login_required
def Postdelete(request):
    post = Post.objects.get(id=request.POST.get('id'))
    post.delete()
    return redirect('home')

@login_required
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
