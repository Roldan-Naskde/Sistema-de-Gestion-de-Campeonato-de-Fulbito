import { useQuery, useQueryClient } from "react-query";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/axios";

export default function Torneos() {
  const queryClient = useQueryClient();
  const navigate = useNavigate();
  const { data, isLoading, error } = useQuery('torneos', async () => (await api.get('tournaments/')).data);

  const eliminarTorneo = async (id) => {
    if (window.confirm("¿Seguro que deseas eliminar este torneo?")) {
      await api.delete(`tournaments/${id}/`);
      queryClient.invalidateQueries('torneos');
    }
  };

  if (isLoading) return <div>Cargando torneos...</div>;
  if (error) return <div>Error al cargar torneos</div>;

  return (
    <div style={{ maxWidth: 900, margin: "2rem auto" }}>
      <h2>Torneos</h2>
      <Link to="/torneos/crear">Crear Torneo</Link>
      <table border="1" cellPadding={6} style={{ width: "100%", borderCollapse: "collapse", marginTop: 16 }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Año</th>
            <th>Descripción</th>
            <th>Inicio</th>
            <th>Fin</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {data.map(t => (
            <tr key={t.id}>
              <td>{t.id}</td>
              <td>{t.name}</td>
              <td>{t.season_year}</td>
              <td>{t.description}</td>
              <td>{t.start_date}</td>
              <td>{t.end_date}</td>
              <td>
                <button onClick={() => navigate(`/torneos/editar/${t.id}`)}>Editar</button>
                <button onClick={() => eliminarTorneo(t.id)} style={{ marginLeft: 8, color: "red" }}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}