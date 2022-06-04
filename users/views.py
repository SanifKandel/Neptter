from django.views.generic import ListView
from django.shortcuts import render 
from users.models import UserDetails

def index(request):
    user_details = UserDetails.objects.all()
    context = {'user_details': user_details}
    print(type(user_details))
    
    return render(request, 'index.html', context)



