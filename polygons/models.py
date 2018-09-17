from django.contrib.gis.db import models


# Create your models here.

class Providers(models.Model):
    name = models.CharField(max_length=128, blank=False)
    email =  models.EmailField(max_length=254, blank=False, unique=True)
    phone_number = models.CharField(max_length=12)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Polygons(models.Model):
    providers = models.ForeignKey(Providers,on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False)
    price = models.FloatField()
    coordinates = models.PolygonField()

    def __str__(self):
        return self.name
