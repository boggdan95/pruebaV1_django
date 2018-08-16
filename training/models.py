from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField


# Create your models here.

class TrainingType(models.Model):
    SECUENCIAL = 'Secuencial'
    RANDOM = 'Aleatorio'
    TYPE_TRAINING = ((SECUENCIAL, "Secuencial"),(RANDOM,"Aleatorio"))
    type_training = models.CharField(max_length=30, choices=TYPE_TRAINING, default=SECUENCIAL)


class TrainingDescription(models.Model):
    TIMES = ((30,30),(45,45),(60,60),(75,75),(90,90),(105,105),(120,120))
    training_type = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    name = models.TextField(default='SOME NAME')
    time = models.IntegerField(choices=TIMES,default=30)
    reps = models.IntegerField(default=10,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(10)
        ])

class TrainingSession(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='User', null=True)
    description = models.ForeignKey(TrainingDescription, on_delete=models.CASCADE)
    results = JSONField() 



class PresetTrainingSession(models.Model):
    training_type = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    name = models.TextField(default='preset training')
    instructions = models.TextField();
    time = models.IntegerField(default=30)
    reps = models.IntegerField(default=10)



