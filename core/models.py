from django.db import models
from django.utils.translation import gettext_lazy as _

# Modelo de Torneo
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    season_year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.season_year}"

# Modelo de Fase
class Stage(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='stages')

    def __str__(self):
        return f"{self.name} - {self.tournament.name}"

# Modelo de Grupo
class Group(models.Model):
    name = models.CharField(max_length=50)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return f"{self.name} - {self.stage.name}"

# Modelo de Equipo
class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    coach_name = models.CharField(max_length=100)
    founded = models.PositiveIntegerField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='teams')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name

# Modelo de Jugador
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Modelo de Estadios
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Modelo de Árbitros
class Referee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Modelo de Partido
class Match(models.Model):
    datetime = models.DateTimeField()
    team_home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team_away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.SET_NULL, null=True, blank=True)
    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_home} vs {self.team_away} ({self.datetime})"

# Modelo de Eventos de Partido
class MatchEvent(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='events')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='events')
    minute = models.PositiveIntegerField()
    event_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.event_type} - {self.player} ({self.minute}')"

# Modelo de Clasificación
class Standing(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='standings')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='standings')
    played = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    drawn = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    gf = models.PositiveIntegerField(default=0)  # Goles a favor
    ga = models.PositiveIntegerField(default=0)  # Goles en contra
    gd = models.IntegerField(default=0)          # Diferencia de goles
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team} - {self.tournament}"
