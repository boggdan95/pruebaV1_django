from django.contrib import admin

# Register your models here.

from .models import TrainingDescription, TrainingSession, PresetTrainingSession

admin.site.register(TrainingDescription)
admin.site.register(TrainingSession)
admin.site.register(PresetTrainingSession)
