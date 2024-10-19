from django.db import models

# Create your models here.
class Company(models.Model):
    """a Company that I should take a look """
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)

class Land(models.Model):
    location = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    size = models.IntegerField()

class Realestate(models.Model):
    location = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    size = models.IntegerField()



