# Generated by Django 2.0.6 on 2018-11-08 21:47

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageGameSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now_add=True)),
                ('results', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('bestTime', models.IntegerField(blank=True, null=True)),
                ('average', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='capturesession',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
