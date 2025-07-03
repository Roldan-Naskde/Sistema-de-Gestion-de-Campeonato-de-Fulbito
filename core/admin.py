from django.contrib import admin
from .models import (
    Tournament, Stage, Group, Team, Player, Venue, Referee, Match, MatchEvent, Standing
)

admin.site.register(Tournament)
admin.site.register(Stage)
admin.site.register(Group)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Venue)
admin.site.register(Referee)
admin.site.register(Match)
admin.site.register(MatchEvent)
admin.site.register(Standing)
