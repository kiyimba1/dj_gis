from unicodedata import name
from django.contrib.gis.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.PointField(null=True)

    def __str__(self) -> str:
        return self.name
