from django.urls import path

from . import views

app_name = 'trainig'
urlpatterns = [
    path('', views.index, name='index'),
]