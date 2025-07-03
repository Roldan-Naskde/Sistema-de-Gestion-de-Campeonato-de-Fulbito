from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Match, Standing, MatchEvent, Player

def actualizar_clasificacion_equipo(equipo, torneo):
    clasificacion, creada = Standing.objects.get_or_create(team=equipo, tournament=torneo)
    partidos = Match.objects.filter(
        tournament=torneo
    ).filter(
        team_home=equipo
    ) | Match.objects.filter(
        tournament=torneo
    ).filter(
        team_away=equipo
    )
    jugados = partidos.count()
    ganados = empatados = perdidos = gf = gc = 0
    for partido in partidos:
        if partido.team_home == equipo:
            gf += partido.home_score
            gc += partido.away_score
            if partido.home_score > partido.away_score:
                ganados += 1
            elif partido.home_score == partido.away_score:
                empatados += 1
            else:
                perdidos += 1
        else:
            gf += partido.away_score
            gc += partido.home_score
            if partido.away_score > partido.home_score:
                ganados += 1
            elif partido.away_score == partido.home_score:
                empatados += 1
            else:
                perdidos += 1
    clasificacion.played = jugados
    clasificacion.won = ganados
    clasificacion.drawn = empatados
    clasificacion.lost = perdidos
    clasificacion.gf = gf
    clasificacion.ga = gc
    clasificacion.gd = gf - gc
    clasificacion.points = ganados * 3 + empatados
    clasificacion.save()

@receiver(post_save, sender=Match)
def actualizar_clasificacion_al_guardar_partido(sender, instance, **kwargs):
    actualizar_clasificacion_equipo(instance.team_home, instance.stage.tournament)
    actualizar_clasificacion_equipo(instance.team_away, instance.stage.tournament)

# Estadísticas individuales de jugadores
@receiver(post_save, sender=MatchEvent)
def actualizar_estadisticas_jugador_al_guardar_evento(sender, instance, **kwargs):
    jugador = instance.player
    eventos = MatchEvent.objects.filter(player=jugador)
    jugador.goals = eventos.filter(event_type__iexact='gol').count()
    jugador.assists = eventos.filter(event_type__iexact='asistencia').count()
    jugador.yellow_cards = eventos.filter(event_type__iexact='amarilla').count()
    jugador.red_cards = eventos.filter(event_type__iexact='roja').count()
    jugador.save()
