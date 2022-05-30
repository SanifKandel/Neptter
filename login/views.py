
# Create your views here.

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
import uuid


def loginProcess(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if username and password !="":
            if user is not None:
                auth_login(request,user)
                return redirect('index')
            else:
                messages.info(request, "Username or password is incorrect")
        else:
            messages.info(request, "Enter username and password")
    else:
        return render(request, 'login.html')

def HomeProcess(request):
    return render(request, 'hello.html')



def send_forget_password_mail(email, token):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://localhost:8000/reset-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list,fail_silently= False)
    return True


def entermailResetpassword(request):


    if request.method == 'POST':
        username = request.POST.get('username')

        if not User.objects.filter(username=username).first():
            messages.add_message(request, messages.ERROR, f'No user found with {username} username.')
            return redirect('/reset-password-enterusername')

        user_obj = User.objects.get(username=username)

        token = str(uuid.uuid4())

        profile_obj = Profile.objects.get(user=user_obj)
        profile_obj.forget_password_token = token
        profile_obj.save()


        send_forget_password_mail(user_obj.email, token)

        messages.add_message(request, messages.SUCCESS, 'An email is sent to user with password changing link.')
        return redirect('/reset-password-enterusername')

    return render(request, 'forget-pw.html')


def resetPassword(request, token):
    profile_obj = Profile.objects.filter(forget_password_token=token).first()
    context = {'user_id': profile_obj.user.id}

    if request.method == 'POST':
        new_password = request.POST.get('password-1')
        confirm_new_password = request.POST.get('password-2')
        user_id = request.POST.get('user_id')

        if user_id is None:
            messages.add_message(request, messages.ERROR, 'No user found with that username.')
            return redirect(f'/reset-password/{token}/')

        if new_password != confirm_new_password:
            messages.add_message(request, messages.ERROR, "Password didn't match ")
            return redirect(f'reset-password/{token}/')

        print(user_id)
        user_obj = User.objects.get(id=user_id)
        print(user_obj)

        user_obj.set_password(new_password)
        user_obj.save()

        return redirect("/reset-password-done")

    return render(request, 'reset-pw.html', context)


def resetpasswordDone(request):
    return render(request, 'reset-password-done.html')
