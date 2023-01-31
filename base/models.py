from django.db import models

class Fillin(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
      
    def __str__(self):
        return self.name


        
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Score(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team',null=True)
    total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.team)

class Week(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

class Match(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE, null=True)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1',null=True)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2',null=True)
    singles1_score = models.CharField(max_length=100, default='none')
    singles2_score = models.CharField(max_length=100, default='none')
    doubles_score = models.CharField(max_length=100, default='none')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winner',null=True)
    def __str__(self):
        return str( 'Week' )+str(self.week)+str( ':' )+str(self.team1)+ str( ' vs ' )+ str(self.team2)