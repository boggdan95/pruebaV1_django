# Generated by Django 2.0.6 on 2018-11-09 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0002_auto_20181108_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorStimuli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
