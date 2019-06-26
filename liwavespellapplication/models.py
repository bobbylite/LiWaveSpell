from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Spot(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.name