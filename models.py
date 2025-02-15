from django.db import models

# Create your models here.
class Geofence(models.Model):
    name=models.CharField(max_length=100)
    latitude=models.FloatField()
    longitude=models.FloatField()
    radius=models.FloatField()

    def __str__(self):
        return self.name

