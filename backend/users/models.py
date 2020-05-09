import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    profilePicture = models.ImageField(upload_to='profile_pics/', blank=True)
    hrResting = models.IntegerField(blank=True, null=True)
    hrMax = models.IntegerField(blank=True, null=True)
    hrAerobicThreshold = models.IntegerField(blank=True, null=True)
    hrLactateThreshold = models.IntegerField(blank=True, null=True)
    athleteCategory = models.IntegerField(
        choices=settings.ATHLETE_CATEGORY_CHOICES, blank=True, null=True)
    isAerobicallyDeficient = models.BooleanField(default=True)
