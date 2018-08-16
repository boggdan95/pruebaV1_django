from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import TrainingDescription



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Opcional.')
    last_name = forms.CharField(max_length=30, help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese un correo valido')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class NewPasswordForm(UserCreationForm):  
    username = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',) 


class TrainingDescriptionForm(forms.ModelForm):
    class Meta:
       model = TrainingDescription
       fields = ('name','training_type', 'time', 'reps')