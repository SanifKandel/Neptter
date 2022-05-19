from django.shortcuts import render

# Create your views here.
def HomeProcess(request):
    return render(request, 'home.html')