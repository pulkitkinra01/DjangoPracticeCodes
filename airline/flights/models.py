from django.db import models

# Create your models here.
# this is going to be a place where we are going to define our models
# Every model is going to be a python class
# 1 model for each of the table we care about storing the data.

# create migrations to make db changes 
# then migrate the changes

class Airport (models.Model ):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight( models.Model ):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination =  models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger( models.Model ):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"