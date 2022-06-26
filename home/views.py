from django.shortcuts import render

from .models import Profile , Post
from .forms import ProfileForm, NewPostForm
from register.models import User
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
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
          data.pic = image.url
        data.save()
       
        messages.success(request, f'Posted Successfully')
        return redirect('home')
    else:
      
      form = NewPostForm(request.POST, request.FILES)
      return render(request, 'home', {'form':form})


def AboutProcess(request):
    return render(request, 'aboutus.html')
