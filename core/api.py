from rest_framework import viewsets
from .models import Tournament, Stage, Group, Team, Player, Venue, Referee, Match, MatchEvent, Standing
from .serializers import (
    TournamentSerializer, StageSerializer, GroupSerializer, TeamSerializer, PlayerSerializer,
    VenueSerializer, RefereeSerializer, MatchSerializer, MatchEventSerializer, StandingSerializer
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchEventViewSet(viewsets.ModelViewSet):
    queryset = MatchEvent.objects.all()
    serializer_class = MatchEventSerializer

class StandingViewSet(viewsets.ModelViewSet):
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def public_standings(request, tournament_id):
    standings = Standing.objects.filter(tournament_id=tournament_id).order_by('-points', '-gd', '-gf')
    serializer = StandingSerializer(standings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def public_schedule(request, stage_id):
    matches = Match.objects.filter(stage_id=stage_id)
    matches_data = []
    for match in matches:
        match_data = MatchSerializer(match).data
        events = MatchEvent.objects.filter(match=match)
        match_data['events'] = MatchEventSerializer(events, many=True).data
        matches_data.append(match_data)
    return Response(matches_data)
