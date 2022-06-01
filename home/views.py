from django.shortcuts import render


# Create your views here.
def HomeProcess(request):
    return render(request, 'home.html')


def ProfileProcess(request):
    return render(request, 'profile.html')


def profile(request):
    return render(request, 'profile_card.html')

def AboutProcess(request):
    return render(request, 'aboutus.html')
