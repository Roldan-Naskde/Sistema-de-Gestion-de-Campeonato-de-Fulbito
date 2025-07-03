from django import forms
from .models import Player, Team, Tournament, Stage, Group, Venue, Referee, Match, MatchEvent

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'birth_date': 'Fecha de nacimiento',
            'position': 'Posición',
            'team': 'Equipo',
            'goals': 'Goles',
            'assists': 'Asistencias',
            'yellow_cards': 'Tarjetas amarillas',
            'red_cards': 'Tarjetas rojas',
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'logo': 'Logo',
            'coach_name': 'Director Técnico',
            'founded': 'Año de fundación',
            'group': 'Grupo',
            'tournament': 'Torneo',
        }

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'season_year': 'Año de temporada',
            'description': 'Descripción',
            'start_date': 'Fecha de inicio',
            'end_date': 'Fecha de fin',
            'created_at': 'Creado en',
        }

class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'order': 'Orden',
            'tournament': 'Torneo',
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'stage': 'Fase',
        }

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'address': 'Dirección',
            'city': 'Ciudad',
            'capacity': 'Capacidad',
        }

class RefereeForm(forms.ModelForm):
    class Meta:
        model = Referee
        fields = '__all__'
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'category': 'Categoría',
        }

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'
        labels = {
            'datetime': 'Fecha y hora',
            'team_home': 'Equipo local',
            'team_away': 'Equipo visitante',
            'venue': 'Estadio',
            'referee': 'Árbitro',
            'home_score': 'Goles local',
            'away_score': 'Goles visitante',
            'stage': 'Fase',
        }

class MatchEventForm(forms.ModelForm):
    class Meta:
        model = MatchEvent
        fields = '__all__'
        labels = {
            'match': 'Partido',
            'player': 'Jugador',
            'minute': 'Minuto',
            'event_type': 'Tipo de evento',
            'description': 'Descripción',
        }
