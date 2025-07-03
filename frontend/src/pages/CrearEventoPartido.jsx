import { useForm } from "react-hook-form";
import { useQuery } from "react-query";
import api from "../api/axios";

export default function CrearEventoPartido() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();

  // Obtener partidos y jugadores para los selects
  const { data: partidos } = useQuery('partidos', async () => (await api.get('matches/')).data);
  const { data: jugadores } = useQuery('jugadores', async () => (await api.get('players/')).data);

  const onSubmit = async (data) => {
    try {
      await api.post("matchevents/", data);
      reset();
      alert("¡Evento registrado!");
    } catch (error) {
      alert("Error al registrar evento");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 500, margin: "2rem auto" }}>
      <h2>Registrar Evento de Partido</h2>
      <div>
        <label>Partido:</label>
        <select {...register("match", { required: "Selecciona el partido" })}>
          <option value="">Selecciona...</option>
          {partidos && partidos.map(p => (
            <option key={p.id} value={p.id}>
              {p.team_home_name || p.team_home} vs {p.team_away_name || p.team_away} ({p.datetime})
            </option>
          ))}
        </select>
        {errors.match && <span>{errors.match.message}</span>}
      </div>
      <div>
        <label>Jugador:</label>
        <select {...register("player", { required: "Selecciona el jugador" })}>
          <option value="">Selecciona...</option>
          {jugadores && jugadores.map(j => (
            <option key={j.id} value={j.id}>{j.first_name} {j.last_name}</option>
          ))}
        </select>
        {errors.player && <span>{errors.player.message}</span>}
      </div>
      <div>
        <label>Minuto:</label>
        <input type="number" {...register("minute", { required: "El minuto es obligatorio" })} />
        {errors.minute && <span>{errors.minute.message}</span>}
      </div>
      <div>
        <label>Tipo de evento:</label>
        <select {...register("event_type", { required: "Selecciona el tipo de evento" })}>
          <option value="">Selecciona...</option>
          <option value="goal">Gol</option>
          <option value="yellow_card">Tarjeta Amarilla</option>
          <option value="red_card">Tarjeta Roja</option>
          <option value="assist">Asistencia</option>
          {/* Agrega más tipos según tu modelo */}
        </select>
        {errors.event_type && <span>{errors.event_type.message}</span>}
      </div>
      <div>
        <label>Descripción:</label>
        <input {...register("description")} />
      </div>
      <button type="submit">Registrar Evento</button>
      {isSubmitSuccessful && <p>¡Evento registrado!</p>}
    </form>
  );
}