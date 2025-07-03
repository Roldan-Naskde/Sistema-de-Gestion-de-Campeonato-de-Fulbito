"""
URL configuration for campeonato_django_sockets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.api import (
    TournamentViewSet, StageViewSet, GroupViewSet, TeamViewSet, PlayerViewSet,
    VenueViewSet, RefereeViewSet, MatchViewSet, MatchEventViewSet, StandingViewSet,
    public_standings, public_schedule
)
from core import views

router = routers.DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'stages', StageViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'referees', RefereeViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'match-events', MatchEventViewSet)
router.register(r'standings', StandingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/public/standings/<int:tournament_id>/', public_standings, name='public_standings'),
    path('api/public/schedule/<int:stage_id>/', public_schedule, name='public_schedule'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.landing_page, name='landing'),
    path('jugadores/', views.mostrar_jugadores, name='mostrar_jugadores'),
    path('equipos/', views.mostrar_equipos, name='mostrar_equipos'),
    path('estadisticas/', views.mostrar_estadisticas, name='mostrar_estadisticas'),
    path('formularios/', views.mostrar_formularios, name='formularios'),
]
