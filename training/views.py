from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from training.forms import SignUpForm, NewPasswordForm, TrainingDescriptionForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = NewPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('usuario')
            if User.objects.filter(username=username).exists():
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Tu constraseña ha sido actualizada satisfactoriamente')
                return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = NewPasswordForm(request.user, request.POST)
    return render(request, 'registration/change_password.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')

@login_required(login_url='login/')
def index(request):
    return render(request, 'training/homepage.html')

@login_required(login_url='login/')
def training(request):
    if request.method == 'POST':
        form = TrainingDescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sesionEntrenamiento')
    else:
        form = TrainingDescriptionForm()
        return render(request, 'training/entrenamiento.html', {'form': form})

@login_required(login_url='login/')
def games(request):
    return render(request, 'training/games.html')

@login_required(login_url='login/')
def configuration(request):
    return render(request, 'training/config.html')

@login_required(login_url='login/')
def faq(request):
    return render(request, 'training/faq.html')

@login_required(login_url='login/')
def contact(request):
    return render(request, 'training/contact.html')

@login_required(login_url='login/')
def sessionTraining(request):
    return render(request, 'training/sesionEntrenamiento.html')
