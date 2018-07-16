from django.urls import path, re_path
from django.contrib.auth import views as auth_views


from . import views

app_name = 'trainig'
urlpatterns = [
    re_path('login', auth_views.LoginView.as_view(), name='login'),
    re_path('register', views.signup, name='signup'),
    re_path('homepage', views.index, name='index'),
    re_path('entrenamiento', views.training, name='training'),
    re_path('games', views.games, name='games'),
    re_path('config', views.configuration, name='configuration'),
    re_path('faq', views.faq, name='faq'),
    re_path('contact', views.contact, name='contact'),
    re_path('sesionEntrenamiento', views.sessionTraining , name='sessionTraining')
]