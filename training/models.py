from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, DecimalValidator
from django.contrib.postgres.fields import JSONField


# Create your models here.

class TrainingDescription(models.Model):
    TIMES = ((30,'30 s'),(45,'45 s'),(60,'60 s'),(75,'75 s'),(90,'90 s'),(105,'105 s'),(120,'120 s'))
    MODULES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'))
    time = models.IntegerField(choices=TIMES,default=30)
    reps = models.IntegerField(default=10,
        validators=[
            DecimalValidator(max_digits=2,decimal_places=1),
            MaxValueValidator(25),
            MinValueValidator(10)
        ])
    modules = models.IntegerField(choices=MODULES,default=1)
    is_random = models.BooleanField(default=False)

class TrainingSession(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='User', null=True)
    description = models.ForeignKey(TrainingDescription, on_delete=models.CASCADE)
    results = JSONField() 



class PresetTrainingSession(models.Model):
    name = models.TextField(default='preset training')
    instructions = models.TextField();
    time = models.IntegerField(default=30)
    reps = models.IntegerField(default=10)
    modules = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])
    is_random = models.BooleanField(default=False)


