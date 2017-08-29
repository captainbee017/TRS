from django.db import models

# Create your models here.

class Location(models.Model):
	street = models.CharField(max_length=200, blank=True)
    city = models.CharField(null=True, max_length=100)
    country = models.CharField(null=True, max_length=100)

    address = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
    	return self.country