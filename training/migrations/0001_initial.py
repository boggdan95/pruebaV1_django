# Generated by Django 2.0.6 on 2018-07-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.PositiveIntegerField()),
            ],
        ),
    ]