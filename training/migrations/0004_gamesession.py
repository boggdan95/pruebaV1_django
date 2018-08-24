# Generated by Django 2.0.6 on 2018-08-22 20:55

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0003_auto_20180820_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now=True)),
                ('results', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.PresetTrainingSession')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]