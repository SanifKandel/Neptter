from django.contrib.auth.decorators import login_required
from register.models import User
from django.shortcuts import render



# Create your views here.
from login.auth import admin_only




@login_required
@admin_only
def admin_dashboard(request):
    user = User.objects.filter(is_staff=0)
    user_count = user.count()
    admin = User.objects.filter(is_staff=1)
    admin_count = admin.count()

    user_info = user.filter(is_staff=0)
    admin_info = admin

    print(admin_info)

    context = {
        'user': user_count,
        'admins': admin_count,
        'user_info': user_info,
        'admin_info': admin_info
    }
    return render(request, 'admin-dashboard.html', context)

