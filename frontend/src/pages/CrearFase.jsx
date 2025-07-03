import { useForm } from "react-hook-form";
import { useQuery } from "react-query";
import api from "../api/axios";

export default function CrearFase() {
  const { register, handleSubmit, reset, formState: { errors, isSubmitSuccessful } } = useForm();
  const { data: torneos } = useQuery('torneos', async () => (await api.get('tournaments/')).data);

  const onSubmit = async (data) => {
    try {
      await api.post("stages/", data);
      reset();
      alert("¡Fase creada!");
    } catch (error) {
      alert("Error al crear fase");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 400, margin: "2rem auto" }}>
      <h2>Registrar Fase</h2>
      <div>
        <label>Nombre:</label>
        <input {...register("name", { required: "El nombre es obligatorio" })} />
        {errors.name && <span>{errors.name.message}</span>}
      </div>
      <div>
        <label>Orden:</label>
        <input type="number" {...register("order", { required: "El orden es obligatorio" })} />
        {errors.order && <span>{errors.order.message}</span>}
      </div>
      <div>
        <label>Torneo:</label>
        <select {...register("tournament", { required: "Selecciona el torneo" })}>
          <option value="">Selecciona...</option>
          {torneos && torneos.map(t => (
            <option key={t.id} value={t.id}>{t.name}</option>
          ))}
        </select>
        {errors.tournament && <span>{errors.tournament.message}</span>}
      </div>
      <button type="submit">Crear Fase</button>
      {isSubmitSuccessful && <p>¡Fase registrada!</p>}
    </form>
  );
}