from django.shortcuts import render
from django.utils import timezone

from django.contrib.auth.models import User



def index(request):
    return render(request, 'training/homepage.html')

def training(request):
    return render(request, 'training/entrenamiento.html')

def games(request):
    return render(request, 'training/games.html')

def configuration(request):
    return render(request, 'training/config.html')

def faq(request):
    return render(request, 'training/faq.html')

def contact(request):
    return render(request, 'training/contact.html')

def sessionTraining(request):
    return render(request, 'training/sesionEntrenamiento.html')
