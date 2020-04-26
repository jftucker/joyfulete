# Generated by Django 3.0.5 on 2020-04-24 03:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('zone', models.IntegerField(choices=[(0, 'Recovery'), (1, 'Zone 1'), (2, 'Zone 2'), (3, 'Zone 3'), (4, 'Zone 4'), (5, 'Zone 5')], default=0)),
                ('completedDateTime', models.DateTimeField(blank=True, null=True)),
                ('tss', models.IntegerField(blank=True, null=True)),
                ('rpe', models.IntegerField(blank=True, null=True)),
                ('joyRating', models.IntegerField(blank=True, null=True)),
                ('workout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='workouts', to='plans.Day')),
            ],
            options={
                'permissions': [('premium', 'Can view all workouts')],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('workouts', models.ManyToManyField(related_name='tags', to='workouts.Workout')),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
    ]
