# Generated by Django 3.0.6 on 2020-06-30 02:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('activity_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('relative_effort', models.IntegerField(blank=True, null=True)),
                ('commute', models.BooleanField(blank=True, null=True)),
                ('gear', models.CharField(blank=True, max_length=50, null=True)),
                ('filename', models.FilePathField(blank=True, null=True, path='/static/activities/')),
                ('athlete_weight', models.FloatField(blank=True, null=True)),
                ('bike_wieght', models.FloatField(blank=True, null=True)),
                ('elapsed_time', models.IntegerField(blank=True, null=True)),
                ('moving_time', models.IntegerField(blank=True, null=True)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('max_speed', models.FloatField(blank=True, null=True)),
                ('average_speed', models.FloatField(blank=True, null=True)),
                ('elevation_gain', models.FloatField(blank=True, null=True)),
                ('elevation_loss', models.FloatField(blank=True, null=True)),
                ('elevation_low', models.FloatField(blank=True, null=True)),
                ('elevation_high', models.FloatField(blank=True, null=True)),
                ('max_grade', models.FloatField(blank=True, null=True)),
                ('average_grade', models.FloatField(blank=True, null=True)),
                ('average_positive_grade', models.FloatField(blank=True, null=True)),
                ('average_negative_grade', models.FloatField(blank=True, null=True)),
                ('average_cadence', models.FloatField(blank=True, null=True)),
                ('max_cadence', models.IntegerField(blank=True, null=True)),
                ('max_heart_rate', models.IntegerField(blank=True, null=True)),
                ('average_heart_rate', models.FloatField(blank=True, null=True)),
                ('max_watts', models.FloatField(blank=True, null=True)),
                ('average_watts', models.FloatField(blank=True, null=True)),
                ('calories', models.FloatField(blank=True, null=True)),
                ('max_temperature', models.IntegerField(blank=True, null=True)),
                ('average_temperature', models.IntegerField(blank=True, null=True)),
                ('total_work', models.FloatField(blank=True, null=True)),
                ('number_of_runs', models.IntegerField(blank=True, null=True)),
                ('uphill_time', models.IntegerField(blank=True, null=True)),
                ('downhill_time', models.IntegerField(blank=True, null=True)),
                ('other_time', models.IntegerField(blank=True, null=True)),
                ('perceived_exertion', models.IntegerField(blank=True, null=True)),
                ('weighted_average_power', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
