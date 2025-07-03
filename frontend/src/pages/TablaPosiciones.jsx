import React from 'react';
import { useQuery } from 'react-query';
import api from '../api/axios';


export default function TablaPosiciones() {
  const { data, error, isLoading } = useQuery('tablaPosiciones', async () => {
    const response = await api.get('teams/standings/');
    return response.data;
  });

  if (isLoading) return <div>Cargando tabla de posiciones...</div>;
  if (error) return <div>Error al cargar la tabla de posiciones</div>;

  return (
    <div>
      <h2>Tabla de Posiciones</h2>
      <table>
        <thead>
          <tr>
            <th>Equipo</th>
            <th>Puntos</th>
            <th>Partidos Jugados</th>
            <th>Victorias</th>
            <th>Empates</th>
            <th>Derrotas</th>
          </tr>
        </thead>
        <tbody>
          {data.map((team) => (
            <tr key={team.id}>
              <td>{team.name}</td>
              <td>{team.points}</td>
              <td>{team.matches_played}</td>
              <td>{team.wins}</td>
              <td>{team.draws}</td>
              <td>{team.losses}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}