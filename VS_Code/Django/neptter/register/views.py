from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

from register.forms import CreateUserForm 

# Create your views here.

def registerProcess(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
        user.save();
        print("User created")
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