from django.shortcuts import render
from django.utils import timezone

from django.contrib.auth.models import User



def HomeView(request):
    user = User.get_username
    return render(request, 'trainig/homepage.html', {'user' : user })

