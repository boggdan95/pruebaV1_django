from django.contrib import admin

# Register your models here.

from .models import TrainingType, TrainingDescription, TrainingSession, PresetTrainingSession

admin.site.register(TrainingType)
admin.site.register(TrainingDescription)
admin.site.register(TrainingSession)
admin.site.register(PresetTrainingSession)
