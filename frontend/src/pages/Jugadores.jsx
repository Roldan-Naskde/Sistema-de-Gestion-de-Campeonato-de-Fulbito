import React from 'react';
import { useQuery } from 'react-query';
import api from '../api/axios';

export default function Jugadores() {
  const { data, isLoading, error } = useQuery('jugadores', async () => {
    const res = await api.get('players/');
    return res.data;
  });

  if (isLoading) return <div>Cargando...</div>;
  if (error) return <div>Error al cargar jugadores</div>;

  return (
    <div>
      <h2>Jugadores</h2>
      <ul>
        {data.map(j => <li key={j.id}>{j.first_name} {j.last_name}</li>)}
      </ul>
    </div>
  );
}