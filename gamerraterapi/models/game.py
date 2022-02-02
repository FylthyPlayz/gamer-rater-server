from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_release = models.IntegerField()
    num_of_players = models.IntegerField()
    estimated_time = models.IntegerField()
    age_recommendation = models.IntegerField()