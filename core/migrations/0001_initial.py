# Generated by Django 5.2.3 on 2025-06-14 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('deporte', models.CharField(default='Fútbol', max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('tipo', models.CharField(choices=[('eliminacion', 'Eliminación'), ('octavos', 'Octavos de final'), ('cuartos', 'Cuartos de final'), ('semifinal', 'Semifinal'), ('final', 'Final')], default='eliminacion', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('A', 'Grupo A'), ('B', 'Grupo B')], default='A', max_length=1)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('fase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to='core.fase')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('ciudad', models.CharField(max_length=100)),
                ('director_tecnico', models.CharField(max_length=100, verbose_name='Director Técnico')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='core.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('posicion', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.PositiveIntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=50, null=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='core.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temporadas', to='core.campeonato')),
            ],
        ),
        migrations.AddField(
            model_name='fase',
            name='temporada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fases', to='core.temporada'),
        ),
    ]
