import uuid
from django.conf import settings
from django.db import models


class Plan(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


class MacroPlan(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    athleteCategory = models.IntegerField(
        choices=settings.ATHLETE_CATEGORY_CHOICES, default=1)
    length = models.IntegerField(blank=True, null=True)


class WeekType(models.Model):
    name = models.CharField(max_length=50)
    macroPlan = models.ForeignKey(
        MacroPlan, on_delete=models.PROTECT, related_name='weeksFramework', blank=True, null=True)
    numStrength = models.IntegerField(blank=True, null=True)
    numActiveRecovery = models.IntegerField(blank=True, null=True)
    numRecovery = models.IntegerField(blank=True, null=True)
    numAerobicBase = models.IntegerField(blank=True, null=True)
    numMuscularEndurance = models.IntegerField(blank=True, null=True)
    numHighIntensity = models.IntegerField(blank=True, null=True)
    percentDistanceStrength = models.FloatField(blank=True, null=True)
    percentDistanceActiveRecovery = models.FloatField(blank=True, null=True)
    percentDistanceRecovery = models.FloatField(blank=True, null=True)
    percentDistanceAerobicBase = models.FloatField(blank=True, null=True)
    percentDistanceMuscularEndurance = models.FloatField(blank=True, null=True)
    percentDistanceHighIntensity = models.FloatField(blank=True, null=True)
    percentVerticalStrength = models.FloatField(blank=True, null=True)
    percentVerticalActiveRecovery = models.FloatField(blank=True, null=True)
    percentVerticalRecovery = models.FloatField(blank=True, null=True)
    percentVerticalAerobicBase = models.FloatField(blank=True, null=True)
    percentVerticalMuscularEndurance = models.FloatField(blank=True, null=True)
    percentVerticalHighIntensity = models.FloatField(blank=True, null=True)


class Week(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    weekType = models.ForeignKey(
        WeekType, on_delete=models.PROTECT, related_name='weekTypes', blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    gain = models.IntegerField(blank=True, null=True)
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, related_name="weeks", blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Week starting {}'.format(self.startDate)


class Day(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    week = models.ForeignKey(
        Week, on_delete=models.PROTECT, related_name='days', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.date.strftime("%A, %b %d %Y")
