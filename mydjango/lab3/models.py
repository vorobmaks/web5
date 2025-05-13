from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=45, blank=False, unique=True)
    stadium = models.CharField(max_length=45, blank=False)
    city = models.CharField(max_length=45)

    def __str__(self):
        return self.team_name