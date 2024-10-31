from django.db import models
from datetime import datetime

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

class Profile(models.Model):
    """a Profile of companies for searching deeper """
    profile_name = models.CharField(max_length=20)
    date_updated = models.DateTimeField(blank=True, null=True, default=datetime.now())
    frequency = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=20, blank=True)
    sector = models.CharField(max_length=20, blank=True)
    dividendMoreThan = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'profiles'
        db_table = 'profile'

class Result(models.Model):
    date_result = models.DateTimeField(blank=True, null=True)
    profile = models.ForeignKey(to=Profile, on_delete=models.PROTECT, related_name="results")



