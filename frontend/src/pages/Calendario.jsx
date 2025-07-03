import React from 'react';
import { useQuery } from 'react-query';
import api from '../api/axios';



export default function Calendario() {
  const { data, isLoading, error } = useQuery('calendario', async () => {
    const res = await api.get('matches/');
    return res.data;
  });

  if (isLoading) return <div>Cargando...</div>;
  if (error) return <div>Error al cargar el calendario</div>;

  return (
    <div>
      <h2>Calendario de Partidos</h2>
      <ul>
        {data.map(match => (
          <li key={match.id}>
            {match.home_team.name} vs {match.away_team.name} - {new Date(match.date).toLocaleDateString()}
          </li>
        ))}
      </ul>
    </div>
  );
}