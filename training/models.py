from django.db import models

from django.db import models
from django.utils import timezone

# Create your models here.

class TrainingType(models.Model):
    id = models.IntegerField()
    key =
    name =



class TrainingDescription(models.Model):
    id = models.IntegerField(default=0)
    type = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    user =
    name = models.
    parameters =



class TrainingSession(models.Model):
    id =
    key =



class PresetTrainingSession(models.Model):
    id =
    key =
    name =
