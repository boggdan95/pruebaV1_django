from django.urls import path, re_path
from django.conf.urls import url

from . import views

app_name = 'trainig'
urlpatterns = [
    path('', views.index, name='index'),
    re_path('homepage', views.index, name='index'),
    re_path('entrenamiento', views.training, name='training'),
    re_path('games', views.games, name='games'),
    re_path('config', views.configuration, name='configuration'),
    re_path('faq', views.faq, name='faq'),
    re_path('contact', views.contact, name='contact'),
]