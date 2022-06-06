from django.shortcuts import render

from .models import Profile
from .forms import ProfileForm, NewPostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

@login_required
def HomeProcess(request):
    return render(request, 'home.html')

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
	user = request.user
	if request.method == "POST":
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.user_name = user
			data.save()
			messages.success(request, f'Posted Successfully')
			return redirect('home')
	else:
		form = NewPostForm()
	return render(request, 'home', {'form':form})


def AboutProcess(request):
    return render(request, 'aboutus.html')
