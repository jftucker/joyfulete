import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse


class Activity(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    upload_id = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=255)
    activity_type = models.CharField(blank=True, null=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    elapsed_time = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    relative_effort = models.IntegerField(blank=True, null=True)
    commute = models.BooleanField(blank=True, null=True)
    gear = models.CharField(blank=True, null=True, max_length=50)
    filename = models.CharField(blank=True, null=True, max_length=255)
    athlete_weight = models.FloatField(blank=True, null=True)
    bike_weight = models.FloatField(blank=True, null=True)
    elapsed_time = models.IntegerField(blank=True, null=True)
    moving_time = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    max_speed = models.FloatField(blank=True, null=True)
    average_speed = models.FloatField(blank=True, null=True)
    elevation_gain = models.FloatField(blank=True, null=True)
    elevation_loss = models.FloatField(blank=True, null=True)
    elevation_low = models.FloatField(blank=True, null=True)
    elevation_high = models.FloatField(blank=True, null=True)
    max_grade = models.FloatField(blank=True, null=True)
    average_grade = models.FloatField(blank=True, null=True)
    average_positive_grade = models.FloatField(blank=True, null=True)
    average_negative_grade = models.FloatField(blank=True, null=True)
    average_cadence = models.FloatField(blank=True, null=True)
    max_cadence = models.IntegerField(blank=True, null=True)
    max_heart_rate = models.IntegerField(blank=True, null=True)
    average_heart_rate = models.FloatField(blank=True, null=True)
    max_watts = models.FloatField(blank=True, null=True)
    average_watts = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    max_temperature = models.IntegerField(blank=True, null=True)
    average_temperature = models.IntegerField(blank=True, null=True)
    total_work = models.FloatField(blank=True, null=True)
    number_of_runs = models.IntegerField(blank=True, null=True)
    uphill_time = models.IntegerField(blank=True, null=True)
    downhill_time = models.IntegerField(blank=True, null=True)
    other_time = models.IntegerField(blank=True, null=True)
    perceived_exertion = models.IntegerField(blank=True, null=True)
    weighted_average_power = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name
