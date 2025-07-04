# Generated by Django 5.2.3 on 2025-07-02 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_estadisticas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('home_score', models.PositiveIntegerField(default=0)),
                ('away_score', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('position', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('season_year', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='temporada',
            name='campeonato',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='estadisticas',
            name='jugador',
        ),
        migrations.RemoveField(
            model_name='fase',
            name='temporada',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='fase',
        ),
        migrations.CreateModel(
            name='MatchEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.PositiveIntegerField()),
                ('event_type', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='referee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.referee'),
        ),
        migrations.AddField(
            model_name='match',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stage'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='core.stage')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='team_logos/')),
                ('coach_name', models.CharField(max_length=100)),
                ('founded', models.PositiveIntegerField(blank=True, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='core.group')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='core.tournament')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='core.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_away',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='core.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='core.team'),
        ),
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.PositiveIntegerField(default=0)),
                ('won', models.PositiveIntegerField(default=0)),
                ('drawn', models.PositiveIntegerField(default=0)),
                ('lost', models.PositiveIntegerField(default=0)),
                ('gf', models.PositiveIntegerField(default=0)),
                ('ga', models.PositiveIntegerField(default=0)),
                ('gd', models.IntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standings', to='core.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standings', to='core.tournament')),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='core.tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venue'),
        ),
        migrations.DeleteModel(
            name='Campeonato',
        ),
        migrations.DeleteModel(
            name='Equipo',
        ),
        migrations.DeleteModel(
            name='Estadisticas',
        ),
        migrations.DeleteModel(
            name='Jugador',
        ),
        migrations.DeleteModel(
            name='Temporada',
        ),
        migrations.DeleteModel(
            name='Fase',
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
    ]
