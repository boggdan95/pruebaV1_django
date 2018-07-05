from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.

class TrainingType(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.PositiveIntegerField()
    name = (('s' , "Secuencial"),('r',"Aleatorio"))



class TrainingDescription(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    user = User.get_username
    name = models.TextField()
    parameters = ('Time', models.IntegerField()),('Iteration', models.IntegerField()),('Hit', models.BooleanField(), type)



class TrainingSession(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    user = User.get_username
    description = models.ForeignKey(TrainingDescription, on_delete=models.CASCADE)
    results = JSONField() 



class PresetTrainingSession(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.IntegerField()
    type = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    parameters = ('Time', models.IntegerField()),('Iteration', models.IntegerField()),('Hit', models.BooleanField(), type)




