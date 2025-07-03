from django.shortcuts import render, redirect
from core.models import Player, Team, Standing, Tournament, Match, MatchEvent
from core.forms import (
    PlayerForm, TeamForm, TournamentForm, StageForm, GroupForm, VenueForm, RefereeForm, MatchForm, MatchEventForm
)

# Vista landing page
def landing_page(request):
    return render(request, 'landing.html')

# Vista para mostrar jugadores
def mostrar_jugadores(request):
    jugadores = Player.objects.all()
    return render(request, 'jugadores.html', {'jugadores': jugadores})

# Vista para mostrar equipos
def mostrar_equipos(request):
    equipos = Team.objects.all()
    return render(request, 'equipos.html', {'equipos': equipos})

# Vista para mostrar estadísticas (tabla de posiciones)
def mostrar_estadisticas(request):
    standings = Standing.objects.select_related('team', 'tournament').all()
    return render(request, 'estadisticas.html', {'estadisticas': standings})

# Vista para registrar jugadores y equipos
def mostrar_formularios(request):
    forms = {
        'player_form': PlayerForm(),
        'team_form': TeamForm(),
        'tournament_form': TournamentForm(),
        'stage_form': StageForm(),
        'group_form': GroupForm(),
        'venue_form': VenueForm(),
        'referee_form': RefereeForm(),
        'match_form': MatchForm(),
        'matchevent_form': MatchEventForm(),
    }
    if request.method == 'POST':
        if 'player_submit' in request.POST:
            player_form = PlayerForm(request.POST)
            if player_form.is_valid():
                player_form.save()
            forms['player_form'] = player_form
        elif 'team_submit' in request.POST:
            team_form = TeamForm(request.POST)
            if team_form.is_valid():
                team_form.save()
            forms['team_form'] = team_form
        elif 'tournament_submit' in request.POST:
            tournament_form = TournamentForm(request.POST)
            if tournament_form.is_valid():
                tournament_form.save()
            forms['tournament_form'] = tournament_form
        elif 'stage_submit' in request.POST:
            stage_form = StageForm(request.POST)
            if stage_form.is_valid():
                stage_form.save()
            forms['stage_form'] = stage_form
        elif 'group_submit' in request.POST:
            group_form = GroupForm(request.POST)
            if group_form.is_valid():
                group_form.save()
            forms['group_form'] = group_form
        elif 'venue_submit' in request.POST:
            venue_form = VenueForm(request.POST)
            if venue_form.is_valid():
                venue_form.save()
            forms['venue_form'] = venue_form
        elif 'referee_submit' in request.POST:
            referee_form = RefereeForm(request.POST)
            if referee_form.is_valid():
                referee_form.save()
            forms['referee_form'] = referee_form
        elif 'match_submit' in request.POST:
            match_form = MatchForm(request.POST)
            if match_form.is_valid():
                match_form.save()
            forms['match_form'] = match_form
        elif 'matchevent_submit' in request.POST:
            matchevent_form = MatchEventForm(request.POST)
            if matchevent_form.is_valid():
                matchevent_form.save()
            forms['matchevent_form'] = matchevent_form
    return render(request, 'formularios.html', forms)
