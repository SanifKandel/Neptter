from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from login.models import Profile
from register.forms import CreateUserForm 

# Create your views here.

def registerProcess(request):
    if request.method == 'POST':
        password1 =request.POST['password1']
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        

        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
        profile = Profile.objects.create(user=user,email=email)
        user.save()
        profile.save()
        print("New user has been created")
        return redirect('login')
   
    else:
        return render(request,"register.html")


       
        # form = CreateUserForm()

        # if request.method == 'POST':
        #     print(request.POST)
        #     print("Got data")
        #     form = CreateUserForm(request.POST)
        #     if  form.is_valid():
        #         print("form valid")
        #         form.save()
        #         print("form saved")
        #         # messages.success("New account created")
        #         return redirect('login')
                
        #     else:
        #         messages.error(request, "Error")
        # context={
        #     'form':form,
        # }
        # return render(request,"register.html",context
