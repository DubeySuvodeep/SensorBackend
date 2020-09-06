# Create your models here.
import uuid
from django.db import models
from django.utils import timezone
from datetime import datetime


class SensorType(models.Model):

    type_of_sensor = models.CharField(max_length=50, null=True, blank=True, unique=True) 

    def __str__(self):
        return self.type_of_sensor