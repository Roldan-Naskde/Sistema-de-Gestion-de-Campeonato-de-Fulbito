import { useQuery } from "react-query";
import api from "../api/axios";

export default function EventosPartido() {
  const { data, isLoading, error } = useQuery('eventos', async () => (await api.get('matchevents/')).data);

  if (isLoading) return <div>Cargando eventos...</div>;
  if (error) return <div>Error al cargar eventos</div>;

  return (
    <div style={{ maxWidth: 900, margin: "2rem auto" }}>
      <h2>Eventos de Partido</h2>
      <table border="1" cellPadding={6} style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Partido</th>
            <th>Jugador</th>
            <th>Minuto</th>
            <th>Tipo</th>
            <th>Descripción</th>
          </tr>
        </thead>
        <tbody>
          {data.map(ev => (
            <tr key={ev.id}>
              <td>{ev.id}</td>
              <td>
                {ev.match} {/* Si tu serializer incluye info de equipos, puedes mostrar: */}
                {/* {ev.match.team_home} vs {ev.match.team_away} */}
              </td>
              <td>
                {ev.player} {/* Si tu serializer incluye info de nombre, puedes mostrar: */}
                {/* {ev.player.first_name} {ev.player.last_name} */}
              </td>
              <td>{ev.minute}</td>
              <td>{ev.event_type}</td>
              <td>{ev.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}