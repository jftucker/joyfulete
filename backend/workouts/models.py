import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse

from plans.models import Day


class Workout(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    workout = models.ForeignKey(Day, on_delete=models.PROTECT, blank=True, null=True, related_name='workouts')
    title = models.CharField(max_length=200)
    description = models.TextField()
    zone = models.IntegerField(choices=settings.ZONE_CHOICES, default=0)
    completedDateTime = models.DateTimeField(blank=True, null=True)
    tss = models.IntegerField(blank=True, null=True)
    rpe = models.IntegerField(blank=True, null=True)
    joyRating = models.IntegerField(blank=True, null=True)
    # gps data?
    # hr data?
    # garmin file?

    class Meta:
        permissions = [
            ("premium", "Can view all workouts")
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('workout_detail', args=[str(self.id)])


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    workouts = models.ManyToManyField(Workout, related_name='tags')

    class Meta:
        ordering = ['tag']

    def __str__(self):
        return self.tag
