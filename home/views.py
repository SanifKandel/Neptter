from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User


# Create your views here.
def HomeProcess(request):
    return render(request, 'home.html')


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
        'profile': ProfileForm(instance=cuser),
    }
    return render(request, 'profile.html', context)


def AboutProcess(request):
    return render(request, 'aboutus.html')
