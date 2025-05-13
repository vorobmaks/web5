from django.db import models

class Season(models.Model):
    season = models.CharField(max_length=45, blank=False)

    def __str__(self):
        return self.season

class Team(models.Model):
    team_name = models.CharField(max_length=45, blank=False, unique=True)
    stadium = models.CharField(max_length=45, blank=False)
    city = models.CharField(max_length=45)

    def __str__(self):
        return self.team_name

class Manager(models.Model):
    train_name = models.CharField(max_length=45, default='Trainer')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=45, blank=False)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.train_name

class Player(models.Model):
    name = models.CharField(max_length=45, blank=False)
    nationality = models.CharField(max_length=45, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    username = models.CharField(max_length=45, unique=True, blank=False)

    def __str__(self):
        return f'{self.name} {self.username}'

class Role(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role = models.CharField(max_length=45)
    position = models.CharField(max_length=45, blank=False)

    class Meta:
        unique_together = ('player', 'role')

class Statistic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goal = models.IntegerField(default=0)
    assist = models.IntegerField(default=0)
    save = models.IntegerField(default=0)
    yellowcard = models.IntegerField(default=0)
    redcard = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.player} Stats'

class Match(models.Model):
    date = models.DateTimeField()
    team1 = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    score_home = models.IntegerField()
    score_away = models.IntegerField()

    def __str__(self):
        return f'{self.team1} - {self.team2}'

class Result(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    winner_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    draw = models.BooleanField(default=False)

class Standing(models.Model):
    position = models.IntegerField()
    points = models.IntegerField()
    games_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    defeats = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team} - {self.season}'

    class Meta:
        unique_together = ('team', 'season')

class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('team', 'match')
