import { useForm } from "react-hook-form";
import { useQuery } from "react-query";
import api from "../api/axios";

export default function CrearPartido() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();

  // Obtener equipos, sedes y árbitros para los selects
  const { data: equipos } = useQuery('equipos', async () => (await api.get('teams/')).data);
  const { data: sedes } = useQuery('sedes', async () => (await api.get('venues/')).data);
  const { data: arbitros } = useQuery('arbitros', async () => (await api.get('referees/')).data);

  const onSubmit = async (data) => {
    try {
      await api.post("matches/", data);
      reset();
      alert("¡Partido creado!");
    } catch (error) {
      alert("Error al crear partido");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 500, margin: "2rem auto" }}>
      <h2>Registrar Partido</h2>
      <div>
        <label>Fecha y hora:</label>
        <input type="datetime-local" {...register("datetime", { required: "La fecha y hora es obligatoria" })} />
        {errors.datetime && <span>{errors.datetime.message}</span>}
      </div>
      <div>
        <label>Equipo local:</label>
        <select {...register("team_home", { required: "Selecciona el equipo local" })}>
          <option value="">Selecciona...</option>
          {equipos && equipos.map(e => (
            <option key={e.id} value={e.id}>{e.name}</option>
          ))}
        </select>
        {errors.team_home && <span>{errors.team_home.message}</span>}
      </div>
      <div>
        <label>Equipo visitante:</label>
        <select {...register("team_away", { required: "Selecciona el equipo visitante" })}>
          <option value="">Selecciona...</option>
          {equipos && equipos.map(e => (
            <option key={e.id} value={e.id}>{e.name}</option>
          ))}
        </select>
        {errors.team_away && <span>{errors.team_away.message}</span>}
      </div>
      <div>
        <label>Sede:</label>
        <select {...register("venue", { required: "Selecciona la sede" })}>
          <option value="">Selecciona...</option>
          {sedes && sedes.map(s => (
            <option key={s.id} value={s.id}>{s.name}</option>
          ))}
        </select>
        {errors.venue && <span>{errors.venue.message}</span>}
      </div>
      <div>
        <label>Árbitro:</label>
        <select {...register("referee")}>
          <option value="">Selecciona...</option>
          {arbitros && arbitros.map(a => (
            <option key={a.id} value={a.id}>{a.first_name} {a.last_name}</option>
          ))}
        </select>
      </div>
      <button type="submit">Crear Partido</button>
      {isSubmitSuccessful && <p>¡Partido registrado!</p>}
    </form>
  );
}