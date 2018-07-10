from django.shortcuts import render
from django.utils import timezone

from django.contrib.auth.models import User



def index(request):
    user = User.get_username
    return render(request, 'training/homepage.html', {'user' : user })



