from django.db import models

# Create your models here.
class Fillin(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
      
    def __str__(self):
        return self.name

class Score(models.Model):

    team = models.CharField(max_length=200, null=True, blank=True)
    total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.team

class Match(models.Model):

    week = models.CharField(max_length=200, null=True, blank=True)
    match1 = models.CharField(max_length=200, null=True, blank=True)
    match2 = models.CharField(max_length=200, null=True, blank=True)
    match3 = models.CharField(max_length=200, null=True, blank=True)
    match4 = models.CharField(max_length=200, null=True, blank=True)
    match5 = models.CharField(max_length=200, null=True, blank=True)
   
    def __str__(self):
        return self.week


