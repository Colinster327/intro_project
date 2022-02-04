from django.db import models

# Create your models here.

class Brands(models.Model):
    name = models.CharField(max_length = 50)

    @property
    def vehicles(self):
        return self.vehicles_set.all()

    def __str__(self):
        return self.name

class Vehicles(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
